# tests/test_routes.py

import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app, db
from app.models import User, Course, Module, ModuleProgress, ModuleNote


def create_test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False  # easier POSTs in tests
    return app


def test_home_page():
    app = create_test_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_feature_page_requires_login():
    """
    /feature should redirect to /auth/login when the user is not logged in.
    """
    app = create_test_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    resp = client.get("/feature")
    assert resp.status_code == 302
    assert "/auth/login" in resp.headers["Location"]


def test_feature_page_after_login():
    """
    After logging in, /feature should render successfully as the
    student's dashboard, even if they have no courses yet.
    """
    app = create_test_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create a user with no courses yet
        user = User(username="student_feature")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        client = app.test_client()

        # Log in
        resp_login = client.post(
            "/auth/login",
            data={"username": "student_feature", "password": "password123"},
            follow_redirects=True,
        )
        assert resp_login.status_code == 200

        # Now access /feature
        resp_feature = client.get("/feature")
        assert resp_feature.status_code == 200
        # Check for a key phrase from the updated template
        assert b"Your Course Progress" in resp_feature.data


def test_login_page_get():
    app = create_test_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    response = client.get("/auth/login")
    assert response.status_code == 200


def test_invalid_login_shows_error():
    """
    Invalid credentials should trigger the flash error message.
    """
    app = create_test_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    resp = client.post(
        "/auth/login",
        data={"username": "fake-user", "password": "wrong-password"},
        follow_redirects=True,
    )

    assert resp.status_code == 200
    # Matches flash("Invalid username or password.", "danger")
    assert b"Invalid username or password." in resp.data


def test_login_and_logout_flow():
    """
    Create a user, log in via /auth/login, then log out via /auth/logout.
    """
    app = create_test_app()
    with app.app_context():
        # Start from a completely clean database
        db.drop_all()
        db.create_all()

        user = User(username="student1", email="student@example.com")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        client = app.test_client()

        # Log in
        response = client.post(
            "/auth/login",
            data={"username": "student1", "password": "password123"},
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert b"Invalid username or password" not in response.data

        # Log out
        response = client.get("/auth/logout", follow_redirects=True)
        assert response.status_code == 200


def test_course_detail_requires_login():
    """
    /courses/<id> should redirect to /auth/login when the user is not logged in.
    """
    app = create_test_app()
    with app.app_context():
        db.create_all()

        user = User(username="student2")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        course = Course(user_id=user.id, title="Intro to Python")
        db.session.add(course)
        db.session.commit()

        course_id = course.id

    client = app.test_client()
    resp = client.get(f"/courses/{course_id}")
    assert resp.status_code == 302
    assert "/auth/login" in resp.headers["Location"]


def test_course_detail_after_login_with_progress():
    """
    After logging in and creating a course + ModuleProgress record,
    /courses/<id> should render the course detail page with progress UI.
    """
    app = create_test_app()
    with app.app_context():
        db.create_all()

        # user
        user = User(username="student3")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        # course
        course = Course(user_id=user.id, title="Intro to Python")
        db.session.add(course)
        db.session.commit()

        # module progress
        mp = ModuleProgress(
            user_id=user.id,
            course_id=course.id,
            module_name="Getting Started",
            percent_complete=80,
        )
        db.session.add(mp)
        db.session.commit()

        course_id = course.id

    client = app.test_client()

    # login first
    resp_login = client.post(
        "/auth/login",
        data={"username": "student3", "password": "password123"},
        follow_redirects=True,
    )
    assert resp_login.status_code == 200

    # now hit the course detail page
    resp_course = client.get(f"/courses/{course_id}")
    assert resp_course.status_code == 200
    assert b"Intro to Python" in resp_course.data
    assert b"Course progress" in resp_course.data
    assert b"My notes for this module" in resp_course.data


def test_course_notes_can_be_saved():
    """
    After logging in, posting to /courses/<id> with note content
    should save the note and show the flash + note text.
    """
    app = create_test_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create user
        user = User(username="note_student")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        # Create course
        course = Course(user_id=user.id, title="Intro to Python")
        db.session.add(course)
        db.session.commit()

        # Create a module so course_detail has a current_module
        module = Module(
            course_id=course.id,
            title="Getting Started",
            order_index=1,
            is_completed=False,
        )
        db.session.add(module)
        db.session.commit()

        course_id = course.id

        client = app.test_client()

        # Log in
        resp_login = client.post(
            "/auth/login",
            data={"username": "note_student", "password": "password123"},
            follow_redirects=True,
        )
        assert resp_login.status_code == 200

        # Post a note to the course detail page
        note_text = "This is a test note from the integration test."
        resp_post = client.post(
            f"/courses/{course_id}",
            data={"content": note_text},
            follow_redirects=True,
        )
        assert resp_post.status_code == 200

        # Check for success flash + note text on the page
        assert b"Notes saved." in resp_post.data
        assert note_text.encode("utf-8") in resp_post.data


def test_404_page_renders():
    app = create_test_app()
    with app.app_context():
        db.create_all()

    client = app.test_client()
    resp = client.get("/this-route-does-not-exist")
    assert resp.status_code == 404
    assert b"Page Not Found" in resp.data  # match text from your 404.html

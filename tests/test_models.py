# tests/test_models.py

import os
import sys

# Make sure Python can find the 'app' package
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app, db
from app.models import User, Course, ModuleProgress, ModuleNote


def create_test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    return app


def test_create_user():
    app = create_test_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        user = User(username="unit_test_user", email="test@example.com")
        user.set_password("dummy-password")

        db.session.add(user)
        db.session.commit()

        fetched = User.query.filter_by(username="unit_test_user").first()
        assert fetched is not None
        assert fetched.username == "unit_test_user"
        assert fetched.check_password("dummy-password") is True


def test_create_course():
    app = create_test_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        # first create an owner user (course.user_id is NOT NULL)
        owner = User(username="owner")
        owner.set_password("dummy-password")
        db.session.add(owner)
        db.session.commit()

        # now create the course tied to that user
        course = Course(user_id=owner.id, title="Intro to Python")
        db.session.add(course)
        db.session.commit()

        fetched = Course.query.filter_by(title="Intro to Python").first()
        assert fetched is not None
        assert fetched.title == "Intro to Python"
        assert fetched.user_id == owner.id


def test_module_progress_and_note():
    """
    Ensure ModuleProgress and ModuleNote records can be created
    and are tied correctly to user/course/module.
    """
    app = create_test_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        # user
        user = User(username="student1")
        user.set_password("password123")
        db.session.add(user)
        db.session.commit()

        # course
        course = Course(user_id=user.id, title="Study Skills & Habits")
        db.session.add(course)
        db.session.commit()

        # module progress record
        mp = ModuleProgress(
            user_id=user.id,
            course_id=course.id,
            module_name="Planning your week",
            percent_complete=50,
        )
        db.session.add(mp)
        db.session.commit()

        # simple module note (uses module_id foreign key, but we can just
        # put a fake id here since Module itself isn’t the focus)
        note = ModuleNote(
            user_id=user.id,
            module_id=1,
            content="Remember to plan before Sunday night.",
        )
        db.session.add(note)
        db.session.commit()

        fetched_mp = ModuleProgress.query.filter_by(
            user_id=user.id, course_id=course.id
        ).first()
        assert fetched_mp is not None
        assert fetched_mp.percent_complete == 50

        fetched_note = ModuleNote.query.filter_by(user_id=user.id).first()
        assert fetched_note is not None
        assert "Remember to plan" in fetched_note.content

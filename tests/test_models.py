# tests/test_models.py

import os
import sys

# Make sure Python can find the 'app' package
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app, db
from app.models import User, Course


def create_test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    return app


def test_create_user():
    app = create_test_app()
    with app.app_context():
        # 👇 ensure a clean DB each time
        db.drop_all()
        db.create_all()

        user = User(username="unit_test_user")
        # need a non-null password_hash
        user.set_password("dummy-password")

        db.session.add(user)
        db.session.commit()

        fetched = User.query.filter_by(username="unit_test_user").first()
        assert fetched is not None
        assert fetched.username == "unit_test_user"
        assert fetched.check_password("dummy-password")


def test_create_course():
    app = create_test_app()
    with app.app_context():
        # 👇 also start clean here
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


# -------------------------------------------------------------
# models.py
# -------------------------------------------------------------
# Purpose:
#   Defines the database models (tables) for the application.
#   These are "blueprints" for how data will be stored in the
#   SQLite database managed by SQLAlchemy.
#
#   For Milestone 1:
#     - The models are defined but not yet used functionally.
#     - They serve to verify that SQLAlchemy and Flask-Login
#       are properly configured and imported without errors.
# -------------------------------------------------------------

# Import the database instance created in app/__init__.py
# "db" is an instance of SQLAlchemy initialized with your Flask app.
from . import db

# Import UserMixin to easily add Flask-Login support.
# This provides default implementations for properties like:
#   - is_authenticated
#   - is_active
#   - is_anonymous
#   - get_id()
# These will be used later when real user authentication is added.
from flask_login import UserMixin


# -------------------------------------------------------------
# User Model
# -------------------------------------------------------------
# Represents an application user (student, instructor, etc.).
# Inherits from:
#   - db.Model: tells SQLAlchemy this is a database table
#   - UserMixin: adds Flask-Login properties for future use
#
# For M1:
#   - This model is non-functional (no real login system yet)
#   - It exists to ensure Flask-Login and SQLAlchemy wiring works.
# -------------------------------------------------------------
class User(db.Model, UserMixin):
    """User model for login management (non-functional for M1)."""

    # Primary key column (unique ID for each user)
    id = db.Column(db.Integer, primary_key=True)

    # Username field (unique, indexed for fast lookup)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)

    # Email address (unique and indexed as well)
    email = db.Column(db.String(120), unique=True, index=True)

    # Password hash placeholder (in future milestones, this will
    # store a securely hashed version of the user's password)
    password_hash = db.Column(db.String(128))  # placeholder only for M1

    # This special method defines how the object appears when printed
    # Example: <User Thao>
    def __repr__(self):
        return f"<User {self.username}>"


# -------------------------------------------------------------
# Course Model
# -------------------------------------------------------------
# Represents a course or learning module in the LMS.
# For M1:
#   - This is a simple stub (not yet connected to User or used).
#   - Included to satisfy the requirement of having one
#     additional domain model besides User.
#
# In later milestones (M2/M3):
#   - You can add relationships (e.g., which user owns/enrolled in which course).
#   - You may store course progress, lessons, etc.
# -------------------------------------------------------------
class Course(db.Model):
    """Simple course model stub (domain model example)."""

    # Primary key column (unique ID for each course)
    id = db.Column(db.Integer, primary_key=True)

    # Course title (cannot be null)
    title = db.Column(db.String(128), nullable=False)

    # Representation of the object when printed
    # Example: <Course CMPE131>
    def __repr__(self):
        return f"<Course {self.title}>"

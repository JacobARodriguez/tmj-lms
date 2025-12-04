from datetime import date
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)

    # streak + reminder tracking
    streak_days = db.Column(db.Integer, default=0)
    last_login_date = db.Column(db.Date, nullable=True)

    # one-to-many: user → courses
    courses = db.relationship("Course", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(128), nullable=False)

    # simple numeric progress
    progress_percent = db.Column(db.Integer, default=0)

    # when finished → used for badge + “completed on”
    completed_at = db.Column(db.Date, nullable=True)

    # one-to-many: course → modules
    modules = db.relationship("Module", backref="course", lazy=True)

    def is_completed(self):
        return self.progress_percent >= 100 or self.completed_at is not None

    def __repr__(self):
        return f"<Course {self.title} ({self.progress_percent}%)>"


class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    order_index = db.Column(db.Integer, default=0)

    # simple flag for now
    is_completed = db.Column(db.Boolean, default=False)

    # one-to-many: module → notes
    notes = db.relationship("ModuleNote", backref="module", lazy=True)

    def __repr__(self):
        return f"<Module {self.title} (course={self.course_id})>"


class ModuleNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"), nullable=False)

    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.Date, default=date.today)

    # relationships back to user/module
    user = db.relationship("User", backref="module_notes")

    def __repr__(self):
        return f"<ModuleNote user={self.user_id} module={self.module_id}>"


class ModuleProgress(db.Model):
    """Tracks user progress for individual course modules."""

    id = db.Column(db.Integer, primary_key=True)

    # Which user this progress belongs to
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Which course this module is part of
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    # Display name of the module
    module_name = db.Column(db.String(128), nullable=False)

    # Completion percentage (0–100)
    percent_complete = db.Column(db.Integer, default=0)

    # Relationships back to User and Course
    user = db.relationship("User", backref="module_progress")
    course = db.relationship("Course", backref="module_progress")

    def __repr__(self) -> str:
        return f"<ModuleProgress {self.module_name} {self.percent_complete}%>"

from datetime import date

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


# =============================================================
# User model
# =============================================================
class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)

    # store a hashed password, never the raw password
    password_hash = db.Column(db.String(256), nullable=False)

    # streak + reminder tracking
    streak_days = db.Column(db.Integer, default=0)
    last_active_date = db.Column(db.Date, nullable=True)

    # one-to-many: user → courses
    courses = db.relationship("Course", backref="user", lazy=True)

    # one-to-many: user → module notes
    module_notes = db.relationship("ModuleNote", backref="user", lazy=True)

    # one-to-many: user → module progress
    module_progress = db.relationship("ModuleProgress", backref="user", lazy=True)

    def set_password(self, password: str) -> None:
        """Hash and store the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Return True if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


# =============================================================
# Course model
# =============================================================
class Course(db.Model):
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    title = db.Column(db.String(128), nullable=False)

    # simple numeric progress (0–100)
    progress_percent = db.Column(db.Integer, default=0)

    # when finished → used for badge + “completed on”
    completed_at = db.Column(db.Date, nullable=True)

    # one-to-many: course → modules
    modules = db.relationship("Module", backref="course", lazy=True)

    # one-to-many: course → module progress records
    module_progress = db.relationship("ModuleProgress", backref="course", lazy=True)

    def is_completed(self) -> bool:
        return self.progress_percent >= 100 or self.completed_at is not None

    def __repr__(self):
        return f"<Course {self.title}>"


# =============================================================
# Module model
# =============================================================
class Module(db.Model):
    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    title = db.Column(db.String(128), nullable=False)
    order_index = db.Column(db.Integer, default=0)

    # simple flag for now
    is_completed = db.Column(db.Boolean, default=False)

    # one-to-many: module → notes
    notes = db.relationship("ModuleNote", backref="module", lazy=True)

    def __repr__(self):
        return f"<Module {self.title}>"


# =============================================================
# ModuleNote model
# =============================================================
class ModuleNote(db.Model):
    __tablename__ = "module_note"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"), nullable=False)

    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"<ModuleNote {self.id}>"


# =============================================================
# ModuleProgress model
# =============================================================
class ModuleProgress(db.Model):
    """Tracks user progress for individual course modules."""

    __tablename__ = "module_progress"

    id = db.Column(db.Integer, primary_key=True)

    # Which user this progress belongs to
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Which course this module is part of
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    # Display name of the module
    module_name = db.Column(db.String(128), nullable=False)

    # Completion percentage (0–100)
    percent_complete = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return f"<ModuleProgress {self.module_name}: {self.percent_complete}%>"

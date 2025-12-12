from datetime import date

# Import Flask tools
from flask import Blueprint, flash, redirect, render_template, request, url_for

# For login-required pages
from flask_login import current_user, login_required

# Database + models
from app import db
from app.models import Course, Module, ModuleNote, ModuleProgress

# Forms
from app.forms import ModuleNoteForm

# --------------------------------------------
# Create Blueprint
# --------------------------------------------
main_bp = Blueprint("main", __name__, template_folder="templates")


def update_course_progress(course, modules):
    """
    Given a Course and list of ModuleProgress entries for that course/user,
    compute and store course-level progress.

    Returns (status, status_label, progress_percent, completion_date_str).
    """

    if modules:
        total = sum(m.percent_complete for m in modules)
        count = len(modules)
        progress_percent = round(total / count)

        if all(m.percent_complete == 100 for m in modules):
            status = "completed"
            status_label = "Completed"
        elif any(m.percent_complete > 0 for m in modules):
            status = "in-progress"
            status_label = "In progress"
        else:
            status = "not-started"
            status_label = "Not started"
    else:
        progress_percent = 0
        status = "not-started"
        status_label = "Not started"

    if status == "completed" and course.completed_at is None:
        course.completed_at = date.today()

    course.progress_percent = progress_percent
    db.session.commit()

    completion_date = (
        course.completed_at.strftime("%b %d, %Y") if course.completed_at else "—"
    )

    return status, status_label, progress_percent, completion_date


def get_reminder_message(user):
    """
    Return a reminder message string if the user has been inactive long enough,
    or None if no reminder should be shown.
    """

    if user is None or user.last_active_date is None:
        return None

    days_since = (date.today() - user.last_active_date).days
    if days_since >= 3:
        return (
            "You haven't studied in "
            f"{days_since} days. Jump back in to keep your streak alive!"
        )

    return None


@main_bp.route("/")
def index():
    """Home page."""
    return render_template("main/index.html")


@main_bp.route("/feature")
def feature():
    """
    Feature demo page wired to real progress data
    for ALL of the student's courses.
    """

    # Get all courses (for the logged-in user if possible)
    if current_user.is_authenticated:
        courses = Course.query.filter_by(user_id=current_user.id).all()
    else:
        courses = Course.query.all()

    course_cards = []

    for course in courses:
        # Load this course's module progress for this user
        query = ModuleProgress.query.filter_by(course_id=course.id)
        if current_user.is_authenticated:
            query = query.filter_by(user_id=current_user.id)
        modules = query.order_by(ModuleProgress.id).all()

        status, status_label, progress_percent, completion_date = (
            update_course_progress(course, modules)
        )

        course_cards.append(
            {
                "course": course,
                "modules": modules,
                "status": status,
                "status_label": status_label,
                "progress_percent": progress_percent,
                "completion_date": completion_date,
            }
        )

    streak_days = current_user.streak_days if current_user.is_authenticated else 0
    reminder_message = (
        get_reminder_message(current_user) if current_user.is_authenticated else None
    )

    return render_template(
        "main/feature.html",
        course_cards=course_cards,
        streak_days=streak_days,
        reminder_message=reminder_message,
    )


# --------------------------------------------
# Route 3: Course Detail Page (notes + real progress)
# --------------------------------------------
@main_bp.route("/courses/<int:course_id>", methods=["GET", "POST"])
@login_required
def course_detail(course_id):
    # Get course or 404
    course = Course.query.get_or_404(course_id)

    # For now, use the first module as the "current" module for notes
    current_module = course.modules[0] if course.modules else None

    form = ModuleNoteForm()
    module_note = None

    if current_module:
        # Look for an existing note for this user + module
        module_note = ModuleNote.query.filter_by(
            user_id=current_user.id,
            module_id=current_module.id,
        ).first()

        # Handle saving notes (POST)
        if form.validate_on_submit():
            if module_note is None:
                module_note = ModuleNote(
                    user_id=current_user.id,
                    module_id=current_module.id,
                    content=form.content.data,
                )
                db.session.add(module_note)
            else:
                module_note.content = form.content.data

            db.session.commit()
            flash("Notes saved.", "success")
            return redirect(url_for("main.course_detail", course_id=course_id))

        # Pre-fill form on GET
        elif request.method == "GET" and module_note is not None:
            form.content.data = module_note.content

    # ---------------------------------
    # Real progress data using ModuleProgress
    # ---------------------------------
    query = ModuleProgress.query.filter_by(course_id=course.id)
    query = query.filter_by(user_id=current_user.id)
    modules = query.order_by(ModuleProgress.id).all()

    status, status_label, progress_percent, completion_date = update_course_progress(
        course, modules
    )

    course_name = course.title if hasattr(course, "title") else "Course"
    streak_days = current_user.streak_days
    reminder_message = get_reminder_message(current_user)

    return render_template(
        "main/course_detail.html",
        course=course,
        course_name=course_name,
        current_module=current_module,
        form=form,
        module_note=module_note,
        modules=modules,
        status=status,
        status_label=status_label,
        progress_percent=progress_percent,
        completion_date=completion_date,
        streak_days=streak_days,
        reminder_message=reminder_message,
    )


# --------------------------------------------
# Error handlers
# --------------------------------------------
@main_bp.app_errorhandler(404)
def not_found(error):
    """
    Custom 404 page for any route handled by this blueprint.
    """
    return render_template("errors/404.html"), 404

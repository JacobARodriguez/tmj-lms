# Import Flask tools
from flask import Blueprint, render_template, request, redirect, url_for, flash

# For login-required pages
from flask_login import login_required, current_user

# Database + models
from app import db
from app.models import Course, Module, ModuleNote, ModuleProgress

# Forms
from app.forms import ModuleNoteForm

# --------------------------------------------
# Create Blueprint
# --------------------------------------------
main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    """Home page."""
    return render_template("main/index.html")


@main_bp.route("/feature")
def feature():
    """Simple feature demo page."""
    return render_template("main/feature.html")


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
    if current_user.is_authenticated:
        query = query.filter_by(user_id=current_user.id)

    modules = query.order_by(ModuleProgress.id).all()

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

    # Placeholder completion date until you track it in the DB
    completion_date = "Nov 26, 2025"

    course_name = course.title if hasattr(course, "title") else "Course"

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
    )

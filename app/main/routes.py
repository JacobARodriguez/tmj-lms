# Import Blueprint to group related routes (pages)
# Import render_template to load and display HTML files
from flask import Blueprint, render_template

# --------------------------------------------
# Create a Blueprint for the "main" part of the site
# --------------------------------------------
main_bp = Blueprint("main", __name__, template_folder="templates")


# --------------------------------------------
# Route 1: Home page ('/')
# --------------------------------------------
@main_bp.route("/")
def index():
    return render_template("main/index.html")


# --------------------------------------------
# Route 2: Feature demo page ('/feature')
# --------------------------------------------
@main_bp.route("/feature")
def feature():
    return render_template("main/feature.html")


# --------------------------------------------
# Route 3: Course Detail Page (fake data for M2 demo)
# --------------------------------------------
@main_bp.route("/courses/<int:course_id>")
def course_detail(course_id):
    # For M2, this uses fake data so the page displays properly
    return render_template(
        "main/course_detail.html",
        course_name="Intro to Python",
        status="completed",
        status_label="Completed",
        progress_percent=100,
        completion_date="Nov 26, 2025",
    )

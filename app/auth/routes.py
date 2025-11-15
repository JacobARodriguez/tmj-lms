# -------------------------------------------------------------
# auth/routes.py
# -------------------------------------------------------------
# Purpose:
#   Handles authentication-related routes.
#   This file defines the /auth/login page that displays and
#   processes the LoginForm.
# -------------------------------------------------------------

from flask import Blueprint, render_template, flash, redirect, url_for
from ..forms import LoginForm  # import the LoginForm class from forms.py

# -------------------------------------------------------------
# Create a Blueprint named "auth"
# -------------------------------------------------------------
# A blueprint lets us group routes together.
# When registered in __init__.py, these routes will be accessible
# under the prefix "/auth" (for example, /auth/login).
# -------------------------------------------------------------
auth_bp = Blueprint("auth", __name__, template_folder="templates")


# -------------------------------------------------------------
# Login route: handles both GET and POST requests
# -------------------------------------------------------------
# URL: /auth/login
# Methods:
#   - GET  → show the login form
#   - POST → validate form data and flash a message
# -------------------------------------------------------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Create a new instance of the login form for every request
    form = LoginForm()

    # ---------------------------------------------------------
    # When user clicks "Sign In", the browser sends a POST request
    # with the form data. Flask-WTF automatically fills the form
    # fields and runs the validators.
    #
    # validate_on_submit() returns True if:
    #   1. The request method is POST, AND
    #   2. All field validators (like DataRequired) pass, AND
    #   3. The CSRF token is valid.
    # ---------------------------------------------------------
    if form.validate_on_submit():
        # This block runs only if the form submission is valid.

        # Flash a one-time feedback message that will appear
        # on the next rendered page (via base.html).
        flash("Login not implemented.")

        # Redirect the user to the home page (main.index).
        # url_for("main.index") dynamically generates the URL "/".
        return redirect(url_for("main.index"))

    # ---------------------------------------------------------
    # If the request was a GET (first page load),
    # or if validation failed (empty fields, etc.),
    # render the login form page again.
    #
    # The template uses {{ form.field() }} syntax to show fields
    # and {{ form.field.errors }} to show validation messages.
    # ---------------------------------------------------------
    return render_template("auth/login.html", form=form)


# -------------------------------------------------------------
# Flow Summary
# -------------------------------------------------------------
# 1. User opens /auth/login  → GET request
#    → validate_on_submit() is False
#    → render login.html with an empty form.
#
# 2. User fills the form and clicks "Sign In" → POST request
#    → validate_on_submit() is True (if valid input)
#    → flash("Login not implemented.") and redirect to "/".
#
# 3. User submits invalid form (empty username/password)
#    → validate_on_submit() is False
#    → re-render login.html showing validation errors.
# -------------------------------------------------------------

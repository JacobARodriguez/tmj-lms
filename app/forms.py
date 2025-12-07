# -------------------------------------------------------------
# forms.py
# -------------------------------------------------------------
# Purpose:
#   Define the LoginForm class that represents the login form
#   shown on /auth/login.  Flask-WTF and WTForms handle
#   form rendering, validation, and CSRF protection.
# -------------------------------------------------------------

# Import FlaskForm, the base class for all forms that use Flask-WTF
from flask_wtf import FlaskForm

# Import specific field types that will appear on the form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField

# Import built-in validators (like "required" fields)
from wtforms.validators import DataRequired, Optional


# -------------------------------------------------------------
# LoginForm class
# -------------------------------------------------------------
# Inherits from FlaskForm so it gains CSRF protection and
# easy integration with templates ({{ form.field() }} syntax).
# This form is created and used inside auth/routes.py, and
# rendered in templates/auth/login.html.
# -------------------------------------------------------------
class LoginForm(FlaskForm):

    # Text input for the username (label shown: "Username")
    # validators=[DataRequired()] means this field cannot be empty;
    # if left blank, validation will fail and display an error.
    username = StringField("Username", validators=[DataRequired()])

    # Password input field (text is hidden as dots)
    # Also required by the DataRequired validator.
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    # Submit button labeled "Sign In"
    # When clicked, it sends a POST request back to /auth/login.
    submit = SubmitField("Sign In")


# -------------------------------------------------------------
# Flow Summary
# -------------------------------------------------------------
# 1. auth/routes.py creates a form instance:
#       form = LoginForm()
# 2. login.html renders the form with Jinja:
#       {{ form.username.label }}  {{ form.username() }}
#       {{ form.password.label }}  {{ form.password() }}
# 3. When the user clicks "Sign In":
#       - The form POSTs back to /auth/login.
#       - form.validate_on_submit() checks validators like DataRequired.
#       - If valid: route flashes "Login not implemented" and redirects.
# 4. Flask-WTF automatically injects a hidden CSRF token
#    (via {{ form.hidden_tag() }}) using SECRET_KEY from config.py.
# -------------------------------------------------------------

# Simple form: one textarea & submit button.
class ModuleNoteForm(FlaskForm):
    content = TextAreaField("Notes", validators=[Optional()])
    submit = SubmitField("Save notes")

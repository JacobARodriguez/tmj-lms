# -------------------------------------------------------------
# config.py
# -------------------------------------------------------------
# Purpose:
#   Holds configuration settings for the Flask application.
#   These settings tell Flask and its extensions (like SQLAlchemy
#   and Flask-WTF) how to behave.
#
#   For Milestone 1:
#     - Defines a placeholder SECRET_KEY (required by Flask-WTF)
#     - Sets up a SQLite database URI for SQLAlchemy
#     - Disables unnecessary modification tracking
#
#   In later milestones (M2/M3):
#     - we might load different configurations (dev/test/prod)
#       or use environment variables for security.
# -------------------------------------------------------------

import os  # Used to work with file paths and environment variables

# BASE_DIR stores the directory path of this config.py file.
# This helps build absolute paths for the database file later.
BASE_DIR = os.path.dirname(__file__)


# -------------------------------------------------------------
# Config class
# -------------------------------------------------------------
# Flask looks for configuration values in this class.
# It can be loaded into the app using:
#   app.config.from_object(Config)
# -------------------------------------------------------------
class Config:
    # ---------------------------------------------------------
    # SECRET_KEY
    # ---------------------------------------------------------
    # Used by Flask (and Flask-WTF) for security features:
    #   - CSRF protection (Cross-Site Request Forgery)
    #   - Session management (signing cookies)
    #
    # Here, we first check if there's an environment variable
    # named "SECRET_KEY" set on the system.
    # If not found, it defaults to "tmj-team-secret" (safe placeholder for M1).
    #
    # NOTE: In production, this should be a long, random, secret value!
    # ---------------------------------------------------------
    SECRET_KEY = os.environ.get("SECRET_KEY", "tmj-team-secret")


    # ---------------------------------------------------------
    # SQLALCHEMY_DATABASE_URI
    # ---------------------------------------------------------
    # The database connection string (URI) used by SQLAlchemy.
    # SQLAlchemy uses this to know *where* the database lives.
    #
    # Here, it checks for an environment variable "DATABASE_URL".
    # If not found, it defaults to a local SQLite database file
    # located inside the app/ directory called "app.db".
    #
    # Example path result:
    #   sqlite:////Users/iris/tmj-lms/app/app.db
    #
    # "sqlite:///" means: use SQLite with a file path instead of a server.
    # ---------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    )


    # ---------------------------------------------------------
    # SQLALCHEMY_TRACK_MODIFICATIONS
    # ---------------------------------------------------------
    # When True, SQLAlchemy tracks every object change and sends
    # signals to the app. That’s unnecessary for most cases and
    # wastes memory, so we disable it by setting this to False.
    # ---------------------------------------------------------
    SQLALCHEMY_TRACK_MODIFICATIONS = False

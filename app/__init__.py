# Core Flask class to create the app
from flask import Flask

# SQLAlchemy = database toolkit (ORM) for models and queries
from flask_sqlalchemy import SQLAlchemy

# Flask-Login = handles logged-in users and @login_required
from flask_login import LoginManager

# Our configuration (SECRET_KEY, SQLite URI, etc.)
from .config import Config

# -----------------------------
# Create extension objects first
# (not attached to any app yet)
# -----------------------------

# Database manager (we'll bind it to the app later)
db = SQLAlchemy()

# Login/session manager (bind later too)
login_manager = LoginManager()

# If a page needs login and the user isn't logged in,
# redirect them to this view (blueprint 'auth', function 'login')
login_manager.login_view = "auth.login"


def create_app():
    """
    App factory: builds and returns a configured Flask app.
    Flask recommends this pattern so tests/tools can create fresh app instances.
    """
    # 1) Make the Flask app object
    app = Flask(__name__)

    # 2) Load configuration (SECRET_KEY, DATABASE URI, etc.)
    app.config.from_object(Config)

    # 3) Attach extensions to this app (now they know about app settings)
    db.init_app(app)
    login_manager.init_app(app)

    # 4) (M1) Minimal user loader for Flask-Login
    #    - Flask-Login calls this to turn a user_id into a user object.
    #    - For M1, we don't load real users yet, so always return None.
    from .models import User  # ensure model imports cleanly in M1

    @login_manager.user_loader
    def load_user(user_id):
        # M1: no real authentication; keep everyone anonymous
        return None

    # 5) Register blueprints (groups of routes)
    #    - 'auth' blueprint handles /auth/... routes (e.g., /auth/login)
    #    - 'main' blueprint handles site pages like / and /feature
    from .auth.routes import auth_bp
    from .main.routes import main_bp

    # All routes in auth_bp will live under /auth (e.g., /auth/login)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Routes in main_bp are registered at root (e.g., / and /feature)
    app.register_blueprint(main_bp)

    # 6) Return the fully configured app so run.py can start it
    return app

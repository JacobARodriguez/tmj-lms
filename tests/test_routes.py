import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app

def test_home_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200

def test_feature_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/feature")
    assert response.status_code == 200

def test_login_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/auth/login")
    assert response.status_code == 200



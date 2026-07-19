"""Authentication tests."""
import pytest


def test_register_user(client):
    """Test user registration."""
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword123",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_user(client):
    """Test user login."""
    # First register
    client.post(
        "/api/auth/register",
        json={
            "email": "test2@example.com",
            "username": "testuser2",
            "password": "testpassword123",
            "full_name": "Test User",
        },
    )
    # Then login
    response = client.post(
        "/api/auth/login",
        json={
            "email": "test2@example.com",
            "password": "testpassword123",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

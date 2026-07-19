"""Repository tests."""
import pytest
from app.repositories.user import UserRepository
from app.services.user import UserService


def test_user_repository_create_and_find(db):
    """Test user repository creation and retrieval."""
    service = UserService()
    user = service.create_user(
        db,
        email="repo_test@example.com",
        username="repotest",
        password="testpassword123",
    )
    
    found_user = UserRepository.find_by_email(db, "repo_test@example.com")
    assert found_user is not None
    assert found_user.email == "repo_test@example.com"

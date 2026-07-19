"""Services tests."""
import pytest
from app.services.user import UserService
from app.services.llm import LLMService


def test_user_service_create(db):
    """Test user service creation."""
    service = UserService()
    user = service.create_user(
        db,
        email="test@example.com",
        username="testuser",
        password="testpassword123",
        full_name="Test User",
    )
    assert user.email == "test@example.com"
    assert user.username == "testuser"


def test_llm_service():
    """Test LLM service."""
    service = LLMService()
    question = service.generate_interview_question("Python", "easy")
    assert isinstance(question, str)
    assert len(question) > 0

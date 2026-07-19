"""Authentication service."""
from passlib.context import CryptContext
from app.auth.jwt import create_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """Authentication service."""

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_token(data: dict) -> str:
        """Create JWT token."""
        return create_token(data)

"""User service."""
from sqlalchemy.orm import Session
from app.database.models.user import User
from app.auth.service import AuthService


class UserService:
    """User service."""

    @staticmethod
    def create_user(db: Session, email: str, username: str, password: str, full_name: str = None) -> User:
        """Create user."""
        hashed_password = AuthService.hash_password(password)
        user = User(
            email=email,
            username=username,
            hashed_password=hashed_password,
            full_name=full_name,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user(db: Session, user_id: int) -> User:
        """Get user by ID."""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        """Get user by email."""
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User:
        """Get user by username."""
        return db.query(User).filter(User.username == username).first()

"""User repository."""
from sqlalchemy.orm import Session
from app.database.models.user import User


class UserRepository:
    """User repository."""

    @staticmethod
    def find_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def find_by_email(db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

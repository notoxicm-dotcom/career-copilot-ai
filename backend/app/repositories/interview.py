"""Interview repository."""
from sqlalchemy.orm import Session
from app.database.models.interview import Interview


class InterviewRepository:
    """Interview repository."""

    @staticmethod
    def create(db: Session, user_id: int, title: str, description: str = None, difficulty: str = "medium") -> Interview:
        interview = Interview(
            user_id=user_id,
            title=title,
            description=description,
            difficulty=difficulty,
        )
        db.add(interview)
        db.commit()
        db.refresh(interview)
        return interview

    @staticmethod
    def find_by_id(db: Session, interview_id: int) -> Interview:
        return db.query(Interview).filter(Interview.id == interview_id).first()

    @staticmethod
    def find_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
        return db.query(Interview).filter(Interview.user_id == user_id).offset(skip).limit(limit).all()

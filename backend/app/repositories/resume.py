"""Resume repository."""
from sqlalchemy.orm import Session
from app.database.models.resume import Resume


class ResumeRepository:
    """Resume repository."""

    @staticmethod
    def create(db: Session, user_id: int, title: str, content: str, file_path: str = None) -> Resume:
        resume = Resume(
            user_id=user_id,
            title=title,
            content=content,
            file_path=file_path,
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)
        return resume

    @staticmethod
    def find_by_id(db: Session, resume_id: int) -> Resume:
        return db.query(Resume).filter(Resume.id == resume_id).first()

    @staticmethod
    def find_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
        return db.query(Resume).filter(Resume.user_id == user_id).offset(skip).limit(limit).all()

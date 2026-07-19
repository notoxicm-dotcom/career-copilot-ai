"""Vacancy repository."""
from sqlalchemy.orm import Session
from app.database.models.vacancy import Vacancy


class VacancyRepository:
    """Vacancy repository."""

    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Vacancy).offset(skip).limit(limit).all()

    @staticmethod
    def find_by_id(db: Session, vacancy_id: int) -> Vacancy:
        return db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()

    @staticmethod
    def search(db: Session, query: str, skip: int = 0, limit: int = 100):
        return db.query(Vacancy).filter(
            (Vacancy.title.ilike(f"%{query}%")) |
            (Vacancy.description.ilike(f"%{query}%")) |
            (Vacancy.company.ilike(f"%{query}%"))
        ).offset(skip).limit(limit).all()

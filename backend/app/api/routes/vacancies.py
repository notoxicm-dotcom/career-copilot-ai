"""Vacancy routes."""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import get_db, get_current_user
from app.schemas.vacancy import VacancyResponse

router = APIRouter()


@router.get("/", response_model=List[VacancyResponse])
async def search_vacancies(
    query: str = Query(...),
    limit: int = Query(20, le=100),
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Search vacancies."""
    # Implementation for searching vacancies
    return [{"id": 1, "title": "Senior Python Developer", "company": "Tech Corp"}]


@router.get("/{vacancy_id}", response_model=VacancyResponse)
async def get_vacancy(
    vacancy_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get vacancy details."""
    # Implementation for getting vacancy
    return {"id": vacancy_id, "title": "Senior Python Developer", "company": "Tech Corp"}

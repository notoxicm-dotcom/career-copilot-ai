"""Vacancy schemas."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class VacancyResponse(BaseModel):
    """Vacancy response."""

    id: int
    title: str
    company: str
    location: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True

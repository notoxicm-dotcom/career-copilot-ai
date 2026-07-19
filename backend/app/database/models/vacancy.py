"""Vacancy model."""
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from datetime import datetime
from app.database.base import Base


class Vacancy(Base):
    """Vacancy model."""

    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    company = Column(String)
    location = Column(String, nullable=True)
    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)
    requirements = Column(Text)
    skills = Column(String)  # comma-separated
    url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

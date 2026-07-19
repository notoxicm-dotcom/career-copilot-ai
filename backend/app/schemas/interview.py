"""Interview schemas."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InterviewCreate(BaseModel):
    """Create interview request."""

    title: str
    description: Optional[str] = None
    difficulty: str = "medium"


class InterviewResponse(BaseModel):
    """Interview response."""

    id: int
    user_id: int
    title: str
    difficulty: str
    score: Optional[float] = None
    created_at: datetime

    class Config:
        from_attributes = True

"""Resume schemas."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ResumeCreate(BaseModel):
    """Create resume request."""

    title: str
    content: str


class ResumeResponse(BaseModel):
    """Resume response."""

    id: int
    user_id: int
    title: str
    score: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

"""User schemas."""
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserResponse(BaseModel):
    """User response."""

    id: int
    email: EmailStr
    username: str
    full_name: str = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

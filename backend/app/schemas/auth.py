"""Authentication schemas."""
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Login request."""

    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    """Register request."""

    email: EmailStr
    username: str
    password: str
    full_name: str = None


class LoginResponse(BaseModel):
    """Login response."""

    access_token: str
    token_type: str
    user_id: int

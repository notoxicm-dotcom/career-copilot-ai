"""User routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.user import UserResponse
from app.services.user import UserService

router = APIRouter()
user_service = UserService()


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get current user info."""
    user = user_service.get_user(db, int(current_user["sub"]))
    return user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID."""
    user = user_service.get_user(db, user_id)
    return user

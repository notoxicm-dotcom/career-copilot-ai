"""Authentication routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.services.user import UserService
from app.auth.service import AuthService

router = APIRouter()
user_service = UserService()
auth_service = AuthService()


@router.post("/register", response_model=LoginResponse)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """Register a new user."""
    user = user_service.get_user_by_email(db, request.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = user_service.create_user(
        db,
        email=request.email,
        username=request.username,
        password=request.password,
        full_name=request.full_name,
    )

    token = auth_service.create_token({"sub": str(user.id), "email": user.email})
    return {"access_token": token, "token_type": "bearer", "user_id": user.id}


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Login user."""
    user = user_service.get_user_by_email(db, request.email)
    if not user or not auth_service.verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = auth_service.create_token({"sub": str(user.id), "email": user.email})
    return {"access_token": token, "token_type": "bearer", "user_id": user.id}

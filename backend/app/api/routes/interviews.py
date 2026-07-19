"""Interview routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import get_db, get_current_user
from app.schemas.interview import InterviewCreate, InterviewResponse
from app.services.llm import LLMService

router = APIRouter()
llm_service = LLMService()


@router.post("/start", response_model=InterviewResponse)
async def start_interview(
    request: InterviewCreate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Start a new interview session."""
    # Implementation for starting interview
    return {"id": 1, "user_id": int(current_user["sub"]), "title": request.title}


@router.get("/{interview_id}", response_model=InterviewResponse)
async def get_interview(
    interview_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get interview details."""
    # Implementation for getting interview
    return {"id": interview_id, "user_id": int(current_user["sub"])}

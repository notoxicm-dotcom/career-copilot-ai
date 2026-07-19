"""Resume routes."""
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.schemas.resume import ResumeCreate, ResumeResponse

router = APIRouter()


@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Upload resume file."""
    # Implementation for uploading resume
    return {"id": 1, "user_id": int(current_user["sub"]), "title": file.filename}


@router.post("/analyze", response_model=dict)
async def analyze_resume(
    resume_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Analyze resume with AI."""
    # Implementation for analyzing resume
    return {"score": 85, "feedback": "Great resume!"}

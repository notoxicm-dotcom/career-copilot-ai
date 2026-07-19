"""Resume service."""
from sqlalchemy.orm import Session
from app.database.models.resume import Resume
from app.repositories.resume import ResumeRepository
from app.services.resume_parsing import ResumeParser


class ResumeService:
    """Resume service."""

    def __init__(self):
        self.repository = ResumeRepository()
        self.parser = ResumeParser()

    def create_resume(self, db: Session, user_id: int, title: str, content: str, file_path: str = None) -> Resume:
        """Create resume."""
        return self.repository.create(db, user_id, title, content, file_path)

    def get_resume(self, db: Session, resume_id: int) -> Resume:
        """Get resume by ID."""
        return self.repository.find_by_id(db, resume_id)

    def get_user_resumes(self, db: Session, user_id: int, skip: int = 0, limit: int = 100):
        """Get user's resumes."""
        return self.repository.find_by_user(db, user_id, skip, limit)

    def parse_resume_file(self, file_path: str) -> dict:
        """Parse resume file and extract information."""
        return self.parser.parse(file_path)

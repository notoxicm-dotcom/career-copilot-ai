"""Interview model."""
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base


class Interview(Base):
    """Interview model."""

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String)
    description = Column(Text, nullable=True)
    difficulty = Column(String, default="medium")  # easy, medium, hard
    score = Column(Float, nullable=True)
    duration = Column(Integer, nullable=True)  # in seconds
    transcript = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="interviews")

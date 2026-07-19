"""Resume parsing service."""
import re
from typing import Dict, List


class ResumeParser:
    """Resume parser for extracting information from resume text."""

    @staticmethod
    def parse(content: str) -> Dict:
        """Parse resume content and extract key information."""
        return {
            "email": ResumeParser.extract_email(content),
            "phone": ResumeParser.extract_phone(content),
            "skills": ResumeParser.extract_skills(content),
            "experience": ResumeParser.extract_experience(content),
            "education": ResumeParser.extract_education(content),
        }

    @staticmethod
    def extract_email(content: str) -> str:
        """Extract email from content."""
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        match = re.search(pattern, content)
        return match.group(0) if match else None

    @staticmethod
    def extract_phone(content: str) -> str:
        """Extract phone number from content."""
        pattern = r"\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}"
        match = re.search(pattern, content)
        return match.group(0) if match else None

    @staticmethod
    def extract_skills(content: str) -> List[str]:
        """Extract skills from content."""
        skills_keywords = [
            "Python", "JavaScript", "Java", "C++", "SQL", "React", "Angular",
            "Django", "FastAPI", "Node.js", "AWS", "Docker", "Kubernetes",
            "Git", "REST API", "GraphQL", "MongoDB", "PostgreSQL"
        ]
        found_skills = []
        for skill in skills_keywords:
            if re.search(r"\b" + skill + r"\b", content, re.IGNORECASE):
                found_skills.append(skill)
        return found_skills

    @staticmethod
    def extract_experience(content: str) -> List[str]:
        """Extract experience from content."""
        experience = []
        lines = content.split("\n")
        for line in lines:
            if any(keyword in line for keyword in ["experience", "work", "job", "position"]):
                experience.append(line.strip())
        return experience[:5]  # Return first 5

    @staticmethod
    def extract_education(content: str) -> List[str]:
        """Extract education from content."""
        education = []
        lines = content.split("\n")
        for line in lines:
            if any(keyword in line for keyword in ["education", "degree", "university", "college", "school"]):
                education.append(line.strip())
        return education[:5]  # Return first 5

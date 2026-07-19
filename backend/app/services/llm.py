"""LLM service."""
from openai import OpenAI
from app.core.config import settings


class LLMService:
    """LLM service for AI interactions."""

    def __init__(self):
        """Initialize LLM service."""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    def generate_interview_question(self, topic: str, difficulty: str = "medium") -> str:
        """Generate interview question."""
        if not settings.OPENAI_API_KEY:
            return f"Sample {difficulty} question about {topic}"

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate a {difficulty} interview question about {topic}",
                    }
                ],
                temperature=0.7,
                max_tokens=200,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating question: {str(e)}"

    def analyze_answer(self, question: str, answer: str) -> dict:
        """Analyze interview answer."""
        if not settings.OPENAI_API_KEY:
            return {"score": 75, "feedback": "Good answer"}

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Question: {question}\n\nAnswer: {answer}\n\nProvide score (0-100) and feedback.",
                    }
                ],
                temperature=0.7,
                max_tokens=300,
            )
            return {"feedback": response.choices[0].message.content}
        except Exception as e:
            return {"error": str(e)}

    def analyze_resume(self, resume_text: str) -> dict:
        """Analyze resume with AI."""
        if not settings.OPENAI_API_KEY:
            return {"score": 80, "feedback": "Good resume"}

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Analyze this resume and provide score (0-100) and detailed feedback:\n\n{resume_text}",
                    }
                ],
                temperature=0.7,
                max_tokens=500,
            )
            return {"analysis": response.choices[0].message.content}
        except Exception as e:
            return {"error": str(e)}

"""LLM factory for creating LLM service instances."""
from app.services.llm import LLMService


class LLMFactory:
    """Factory for creating LLM services."""

    _instances = {}

    @staticmethod
    def get_service(service_type: str = "openai") -> LLMService:
        """Get LLM service instance."""
        if service_type not in LLMFactory._instances:
            if service_type == "openai":
                LLMFactory._instances[service_type] = LLMService()
        return LLMFactory._instances[service_type]

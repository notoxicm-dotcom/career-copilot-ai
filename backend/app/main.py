"""Main FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, users, interviews, resumes, vacancies
from app.core.config import settings
from app.api.middleware import ErrorHandlerMiddleware

app = FastAPI(
    title="Career Copilot AI",
    description="AI-powered career preparation platform",
    version="0.1.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error Handler Middleware
app.add_middleware(ErrorHandlerMiddleware)

# API Routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(interviews.router, prefix="/api/interviews", tags=["interviews"])
app.include_router(resumes.router, prefix="/api/resumes", tags=["resumes"])
app.include_router(vacancies.router, prefix="/api/vacancies", tags=["vacancies"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Career Copilot AI",
        "version": "0.1.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

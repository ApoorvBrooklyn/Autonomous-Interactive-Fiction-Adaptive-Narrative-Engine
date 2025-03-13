# backend/api/router.py
from fastapi import APIRouter
from .story_generator import generate_story

router = APIRouter()

@router.get("/generate_story/")
def get_story(user_input: str):
    """API Endpoint: Get the next part of the story."""
    return {"story": generate_story(user_input)}

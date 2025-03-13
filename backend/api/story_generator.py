# backend/api/story_generator.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(user_input: str):
    """Generates a story segment based on user input."""
    prompt = f"You are an AI storyteller. Guide the user through an interactive adventure. The user says: {user_input}"
    
    response = client.chat.completions.create(
        model="gpt-4",  # Ensure you specify a valid model
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": user_input}
        ],
    )
    
    return response.choices[0].message.content
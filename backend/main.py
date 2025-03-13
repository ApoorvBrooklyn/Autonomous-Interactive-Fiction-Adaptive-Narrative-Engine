# backend/main.py
from fastapi import FastAPI
from api.router import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Story Generator"}

# Run the server with:
# uvicorn backend.main:app --reload

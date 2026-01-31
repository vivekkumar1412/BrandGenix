from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="BrandGenix AI") 

#Connect routes in main.py
from app.routes import router as api_router 
app.include_router(api_router, prefix="/api")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "BrandGenix backend is running"
    }

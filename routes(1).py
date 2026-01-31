from fastapi import APIRouter
from pydantic import BaseModel
from app.ai_service import generate_brand_names, generate_marketing_content  # import both

router = APIRouter()

# Brand Name Generation
class BrandRequest(BaseModel):
    prompt: str
    n_names: int = 3

@router.post("/generate-brand")
def generate_brand(data: BrandRequest):
    result = generate_brand_names(data.prompt, data.n_names)
    return {"brand_names": result}

# Marketing Content Generation
class ContentRequest(BaseModel):
    brand_description: str
    tone: str
    content_type: str  # e.g., "product description", "ad copy"
    language: str = "en"

@router.post("/generate-content")
def generate_content(data: ContentRequest):
    result = generate_marketing_content(
        brand_description=data.brand_description,
        tone=data.tone,
        content_type=data.content_type,
        language=data.language
    )
    return {"generated_content": result}

class BrandingAssistRequest(BaseModel):
    brand_name: str
    industry: str

@router.post("/branding-assistant")
def branding_assist(data: BrandingAssistRequest):
    result = branding_assistant(data.brand_name, data.industry)
    return {"analysis": result}
class SentimentRequest(BaseModel):
    text: str

@router.post("/sentiment")
def analyze_sentiment(data: SentimentRequest):
    result = sentiment_analysis(data.text)
    return {"sentiment": result}

from groq import Groq
import os
from dotenv import load_dotenv
from pathlib import Path

# ---------------------------------------------------
# Load .env explicitly from project root
# ---------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# ---------------------------------------------------
# Read environment variables
# ---------------------------------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# ---------------------------------------------------
# Hard validation (fail fast if missing)
# ---------------------------------------------------
if not GROQ_API_KEY:
    raise RuntimeError(
        "❌ GROQ_API_KEY not found. Make sure .env exists in project root "
        "and contains GROQ_API_KEY=..."
    )

# ---------------------------------------------------
# Initialize Groq client
# ---------------------------------------------------
client = Groq(api_key=GROQ_API_KEY)

# ---------------------------------------------------
# Brand Name Generation
# ---------------------------------------------------
def generate_brand_names(prompt: str, n_names: int = 3):
    """
    Generate creative brand names using Groq LLaMA model.
    """
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}. Generate {n_names} creative brand names."
            }
        ]
    )
    return response.choices[0].message.content


# ---------------------------------------------------
# Marketing Content Generation
# ---------------------------------------------------
def generate_marketing_content(
    brand_description: str,
    tone: str = "professional",
    content_type: str = "product description",
    language: str = "en"
):
    """
    Generate marketing / branding content using Groq LLaMA model.
    """
    prompt = (
        f"Write a {content_type} in {language} with a {tone} tone "
        f"for the following brand:\n{brand_description}"
    )

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def branding_assistant(brand_name: str, industry: str):
    prompt = f"""
You are a branding expert.
Analyze the brand name "{brand_name}" for the {industry} industry.
Give:
1. Strengths
2. Weaknesses
3. Target audience fit
4. Overall recommendation
"""

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
def sentiment_analysis(text: str):
    prompt = f"""
Analyze the sentiment of the following text.
Classify as Positive, Neutral, or Negative and explain briefly.

Text:
{text}
"""

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
def generate_logo_concept(brand_name: str):
    """
    Generates a professional logo design concept using AI.
    This is TEXT-BASED (no image generation).
    """

    prompt = f"""
    You are a professional brand designer.

    Create a logo concept for a brand named "{brand_name}".

    Provide:
    1. Logo shape
    2. Color palette (with reasoning)
    3. Typography style
    4. Icon or symbol idea
    5. Overall brand feeling

    Keep it concise and professional.
    """

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

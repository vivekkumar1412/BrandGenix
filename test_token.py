import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from current directory

hf_token = os.getenv("HF_API_KEY")

print("HF_API_KEY value:", hf_token)

if hf_token is None:
    raise RuntimeError("HF_API_KEY not loaded. Check .env location!")

print("✅ Token successfully loaded")


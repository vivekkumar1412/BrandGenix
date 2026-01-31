import requests

# Base URL of your FastAPI server
BASE_URL = "http://127.0.0.1:8000/api"

# --- Step 1: Generate brand names ---
brand_payload = {"prompt": "AI startup", "n_names": 3}
brand_response = requests.post(f"{BASE_URL}/generate-brand", json=brand_payload)

if brand_response.status_code == 200:
    brand_names = brand_response.json()["brand_names"]
    print("\n--- Brand Names ---\n")
    print(brand_names)
else:
    print("Error generating brand names:", brand_response.text)

# --- Step 2: Generate content based on brand description ---
content_payload = {
    "brand_description": "AI startup that builds smart assistants",
    "tone": "professional",
    "content_type": "product description",
    "language": "en"
}
content_response = requests.post(f"{BASE_URL}/generate-content", json=content_payload)

if content_response.status_code == 200:
    content = content_response.json()["generated_content"]
    print("\n--- Generated Content ---\n")
    print(content)
else:
    print("Error generating content:", content_response.text)

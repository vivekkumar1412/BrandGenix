import requests

BASE_URL = "http://127.0.0.1:8000"

def generate_brand(prompt, n_names=3):
    resp = requests.post(
        f"{BASE_URL}/api/generate-brand",
        json={"prompt": prompt, "n_names": n_names}
    )
    if resp.status_code == 200:
        print("Brand Names:\n", resp.json()["brand_names"])
    else:
        print("Error:", resp.text)

def generate_content(description, tone="professional", content_type="product description", language="en"):
    resp = requests.post(
        f"{BASE_URL}/api/generate-content",
        json={
            "brand_description": description,
            "tone": tone,
            "content_type": content_type,
            "language": language
        }
    )
    if resp.status_code == 200:
        print("Generated Content:\n", resp.json()["generated_content"])
    else:
        print("Error:", resp.text)

if __name__ == "__main__":
    print("\n--- Brand Name Demo ---")
    generate_brand("AI startup", 3)

    print("\n--- Content Generation Demo ---")
    generate_content("AI startup that builds smart assistants")

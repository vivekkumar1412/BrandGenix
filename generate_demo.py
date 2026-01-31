import requests

# Your API endpoint
url = "http://127.0.0.1:8000/api/generate-brand"

# Prompt and number of names
data = {
    "prompt": "AI startup",
    "n_names": 3 #number of names
}

# Call the API
response = requests.post(url, json=data)

if response.status_code == 200:
    brand_names = response.json().get("brand_names", "")
    print(f"\nPrompt: {data['prompt']}\nGenerated Brand Names:\n")
    # Split by line if multiple names are included
    for i, name in enumerate(brand_names.split("\n"), 1):
        if name.strip():  # skip empty lines
            print(f"{i}. {name.strip()}")
else:
    print("Error:", response.status_code, response.text)

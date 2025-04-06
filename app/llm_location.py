import requests
from app.config import GROQ_API_KEY
import re 
from functools import lru_cache

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@lru_cache(maxsize=1000)
def extract_locations_from_query(prompt: str) -> list:
    print("API_KEY",GROQ_API_KEY)
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "llama3-8b-8192",
        "messages": [
           {"role": "system", "content":(
                "You are an assistant that extracts up to 3 Indian city, state, or region names from a short query. "
                "The input may contain typos due to fast typing by tele-callers. "
                "Respond ONLY with a plain comma-separated list. No explanations or extra text."
            ) },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 100
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=body)
    print("API_RESPONSE",response)
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        print("LLM raw response:", content)
        places = re.findall(r"[a-zA-Z ]{3,}", content)
        return [loc.strip().lower() for loc in re.split(r',|\\n|\\r', content) if loc.strip()]
    else:
        print("Error:", response.status_code, response.text)
        return []

    
       
   
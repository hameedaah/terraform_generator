import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script_with_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',  
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Error: Failed to generate Terraform script."
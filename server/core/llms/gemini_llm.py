import os 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

GEMINI_MODEL_ID = "gemini-2.5-pro"
gemini_model = genai.GenerativeModel(GEMINI_MODEL_ID)


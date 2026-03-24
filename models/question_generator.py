import google.generativeai as genai
from utils.helpers import get_fallback_question

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_question(role, difficulty):

    prompt = f"""
Generate ONE {difficulty} interview question for a {role}.
Only return the question.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print("Gemini Error:", e)
        return get_fallback_question(role, difficulty)
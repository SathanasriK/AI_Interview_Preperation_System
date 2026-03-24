import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_better_answer(question):

    prompt = f"""
Give a strong interview answer for this question:

{question}

Answer professionally and clearly.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except:
        return "A detailed answer explaining the concept with examples."
import google.generativeai as genai

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_feedback(answer):

    prompt = f"""
You are an interview coach.

Candidate Answer:
{answer}

Give short feedback.

Format:

Strengths:
- point

Improvements:
- point
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        print("Gemini Feedback Error:", e)

        return """
Strengths:
• Attempted the answer

Improvements:
• Add more detailed explanation
• Include examples
"""
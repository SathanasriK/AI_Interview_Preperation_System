import google.generativeai as genai

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def evaluate_answer(question, answer):

    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return format:

Score: X/10

Strengths:
- point

Improvements:
- point
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        print("Gemini Evaluator Error:", e)

        score = min(len(answer.split()) // 10, 10)

        return f"""
Score: {score}/10

Strengths:
• Attempted the answer

Improvements:
• Add more technical explanation
"""
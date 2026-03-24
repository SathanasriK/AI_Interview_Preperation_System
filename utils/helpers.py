import json
import random

def get_fallback_question(role, difficulty):

    try:
        with open("data/hr_questions.json") as f:
            hr = json.load(f)

        with open("data/technical_questions.json") as f:
            tech = json.load(f)

        hr_questions = hr.get(role, {}).get(difficulty, [])
        tech_questions = tech.get(role, {}).get(difficulty, [])

        questions = hr_questions + tech_questions

        if questions:
            return random.choice(questions)

        return "Explain the difference between SQL and NoSQL."

    except Exception as e:
        print("Dataset error:", e)
        return "Explain the difference between SQL and NoSQL."
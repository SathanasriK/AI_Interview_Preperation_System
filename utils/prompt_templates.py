QUESTION_PROMPT = """
Generate an interview question for the role: {role}
"""

EVALUATION_PROMPT = """
Evaluate the answer for the interview question.

Question: {question}
Answer: {answer}

Provide score out of 10.
"""
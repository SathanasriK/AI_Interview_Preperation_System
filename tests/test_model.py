from models.question_generator import generate_question

def test_question():

    q = generate_question("Software Engineer")

    assert q is not None
import streamlit as st
from models.question_generator import generate_question
from models.evaluator import evaluate_answer
from models.feedback_generator import generate_feedback
from models.answer_generator import generate_better_answer

from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Interview Preparation System",
    page_icon="🎤",
    layout="wide"
)


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#667eea,#764ba2);
    color:white;
}

/* Title */
.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
}

/* Subtitle */
.subtitle {
    text-align:center;
    font-size:18px;
    margin-bottom:30px;
}

/* Question card */
.card {
    background: rgba(255,255,255,0.15);
    padding:20px;
    border-radius:12px;
    margin-bottom:15px;
    border-left:5px solid #ffd166;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg,#ff9966,#ff5e62);
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:10px;
    font-size:16px;
}

.stButton>button:hover {
    transform:scale(1.05);
}

/* Footer */
.footer {
    text-align:center;
    margin-top:40px;
    font-size:14px;
    opacity:0.8;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class='title'>🎤 AI Interview Preparation System</div>
<div class='subtitle'>Practice technical interviews with AI powered evaluation</div>
""",
unsafe_allow_html=True
)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=120)

    st.title("Interview Setup")

    roles = [
        "Software Engineer",
        "Data Scientist",
        "Frontend Developer",
        "Backend Developer",
        "Machine Learning Engineer",
        "Other"
    ]

    selected_role = st.selectbox("Select Role", roles)

    if selected_role == "Other":
        role = st.text_input("Enter your role")
    else:
        role = selected_role

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    num_questions = st.slider(
        "Number of Questions",
        1,
        10,
        3
    )

    start = st.button("Start Interview")


# ---------------- START INTERVIEW ---------------- #

if start:

    if role == "":
        st.warning("Please enter a role")

    else:

        st.session_state.questions = [
            generate_question(role, difficulty)
            for _ in range(num_questions)
        ]

        st.session_state.scores = [0]*num_questions


# ---------------- QUESTIONS ---------------- #

if "questions" in st.session_state:

    st.header("Interview Questions")

    for i, question in enumerate(st.session_state.questions):

        st.progress((i+1)/len(st.session_state.questions))

        st.markdown(
            f"""
            <div class="card">
            <b>Question {i+1}</b><br><br>
            {question}
            </div>
            """,
            unsafe_allow_html=True
        )

        answer = st.text_area(
            "Your Answer",
            key=f"text{i}"
        )

        st.write("Or answer by voice 🎤")

        audio = mic_recorder(
            start_prompt="Start Recording",
            stop_prompt="Stop Recording",
            key=f"mic{i}"
        )

        if audio:

            recognizer = sr.Recognizer()

            try:

                with sr.AudioFile(audio["path"]) as source:
                    audio_data = recognizer.record(source)

                text = recognizer.recognize_google(audio_data)

                st.success("Voice converted to text")

                st.write(text)

                answer = text

            except:
                st.error("Voice recognition failed")


        if st.button(f"Evaluate Answer {i+1}"):

            if answer == "":
                st.warning("Please enter an answer")

            else:

                score = evaluate_answer(question, answer)

                feedback = generate_feedback(answer)

                better = generate_better_answer(question)

                st.subheader("Evaluation")
                st.write(score)

                st.subheader("Feedback")
                st.write(feedback)

                st.subheader("Better Answer")
                st.write(better)

                try:
                    value = int(score.split("/")[0].split(":")[-1].strip())
                except:
                    value = 5

                st.session_state.scores[i] = value


# ---------------- FINAL REPORT ---------------- #

if "scores" in st.session_state:

    if st.button("Generate Final Interview Report"):

        total = sum(st.session_state.scores)

        max_score = len(st.session_state.scores) * 10

        percent = (total/max_score)*100

        st.markdown("---")

        st.markdown(
            f"""
            <div class="card" style="text-align:center">
            <h2>Interview Report</h2>
            <h3>Total Score: {total} / {max_score}</h3>
            <h3>Performance: {percent:.1f}%</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        if percent >= 80:
            st.success("Excellent Performance")
        elif percent >= 60:
            st.info("Good Performance")
        else:
            st.warning("Needs Improvement")


# ---------------- FOOTER ---------------- #

st.markdown(
"""
<div class="footer">
Built with ❤️ using Streamlit + Gemini AI
</div>
""",
unsafe_allow_html=True
)
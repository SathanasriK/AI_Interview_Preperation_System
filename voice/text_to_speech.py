from gtts import gTTS
import os

def speak_question(question):

    tts = gTTS(question)

    tts.save("question.mp3")

    os.system("start question.mp3")
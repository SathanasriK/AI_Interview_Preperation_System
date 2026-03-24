import speech_recognition as sr

def listen_answer():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    text = r.recognize_google(audio)

    return text
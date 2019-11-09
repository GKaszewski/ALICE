import speech_recognition as sr

def test():
    r = sr.Recognizer()

    with sr.Microphone() as src: 
        audio = r.listen(src)

        if 'hello' in r.recognize_google(audio):
            print('Hello indeed!')
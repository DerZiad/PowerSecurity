import speech_recognition
import os
from playsound import playsound
from gtts import gTTS
import threading


class SoundManager:
    def __init__(self):
        self.file = []

    def task(self,text,lang, slow):
        lock = threading.Lock()
        lock.acquire()
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")
        output = gTTS(text=text, lang=lang, slow=slow)
        output.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")
        lock.release()
    def speech(self,text="Hello world", lang="en", slow=True):
        t1 = threading.Thread(target=self.task,args=(text,lang,slow))
        t1.start()
    def recognize(self):
        recognizer = speech_recognition.Recognizer()

        while True:
            try:
                with speech_recognition.Microphone() as mic:

                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    text = recognizer.recognize_google(audio)
                    text = text.lower()

                    print(f"Recogniezd {text}")
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                print("Error")
                continue
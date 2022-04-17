import speech_recognition
import os
from playsound import playsound
from gtts import gTTS
import random
import threading

max = 1
min = 0


class Sound:
    def __init__(self, text, lang, slow, priority):
        self.text = text
        self.lang = lang
        self.slow = slow
        self.priority = priority


class SoundManager(threading.Thread):
    def generate(self):
        name = ""
        for i in range(0,6):
            char = random.randint(65,122)
            name += chr(char)
        return name
    def __init__(self):
        threading.Thread.__init__(self)
        self.pool = []
        self.isPlaying = False
    def run(self):
        while True:
            if not self.isPlaying:
                try:
                    soundTemp = self.pool.pop()
                    self.play(soundTemp.text, soundTemp.lang, soundTemp.slow)
                except IndexError:
                   pass
    def addSound(self,sound:Sound):
        if sound.priority == max:
            self.pool.clear()
        self.pool.append(sound)

    def play(self, text="Hello world", lang="en", slow=True):
        name = self.generate()
        while os.path.exists(name):
            name = self.generate()
        output = gTTS(text=text, lang=lang, slow=slow)
        output.save("{}.mp3".format(name))
        playsound("{}.mp3".format(name))
        os.remove("{}.mp3".format(name))
    '''def recognize(self):
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

    '''
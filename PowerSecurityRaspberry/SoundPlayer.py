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
        self.played = False


class SoundManager(threading.Thread):
    def generate(self):
        name = ""
        for i in range(0, 6):
            char = random.randint(97, 122)
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
                    soundTemp.played=True
                except IndexError:
                    pass

    def addSound(self, sound: Sound):
        self.pool.clear()
        self.pool.append(sound)

    def play(self, text="Hello world", lang="en", slow=True):
        self.isPlaying = True
        name = self.generate()
        while os.path.exists(name):
            name = self.generate()
        output = gTTS(text=text, lang=lang, slow=slow)
        output.save("{}.mp3".format(name))
        playsound("{}.mp3".format(name))
        os.remove("{}.mp3".format(name))
        self.isPlaying = False

class PowerRecognizer:
    def __init__(self,soundManager:SoundManager):
        self.recognizer = speech_recognition.Recognizer()
        self.soundManager = soundManager
        #Configure
        print("Please select one microphone")
        for i,name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            print("{}) - {}".format(i + 1,name))
        self.microphoneIndex = int(input("Enter microphone index :"))
    def recognize(self):
        try:
            with speech_recognition.Microphone(device_index=(self.microphoneIndex-1)) as mic:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("Listening")
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio)
                print(text)
                text = text.lower()

                return text
        except speech_recognition.UnknownValueError:
            sound = Sound("Can you repeat i cannot hear you", "en", False, max)
            self.soundManager.addSound(sound)
            while not sound.played:
                pass

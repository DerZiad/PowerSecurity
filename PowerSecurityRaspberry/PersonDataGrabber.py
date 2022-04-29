from SoundPlayer import *
import threading
import re
import time
import os

class PersonGrabber(threading.Thread):

    def generate(self):
        name = ""
        for i in range(0, 6):
            char = random.randint(97, 122)
            name += chr(char)
        return name

    def __init__(self, soundManager):
        threading.Thread.__init__(self)
        self.started = False
        self.soundManager = soundManager
        self.name = ""
    def run(self):
        while True:
            if self.started:
                name = self.generate()
                while os.path.exists(name):
                    name = self.generate()
                self.name = name
                sound = Sound("Can you say your name : my name is Alexis Texas:", "en", True, max)
                self.soundManager.addSound(sound)
                while not sound.played:
                    pass
                text = recognize()
                lastName, firstName = self.formatText(text)
                if firstName != "" and lastName != "":
                    sound = Sound("Welcome " + firstName + ", Enjoy your day", "en", True, max)
                    self.soundManager.addSound(sound)
                    while not sound.played:
                        pass
                    time.sleep(1000)
                    self.close()

    def formatText(self, text):
        reg = "my name is [A-Za-z]* [A-Za-z]*"
        if re.match(reg, text):
            words = text.split(" ")
            firstName = words[3]
            lastName = words[4]
            return lastName, firstName
        return "", ""

    def close(self):
        self.started = False
        if os.path.exists(self.name):
            os.remove(self.name)
        self.name = ""

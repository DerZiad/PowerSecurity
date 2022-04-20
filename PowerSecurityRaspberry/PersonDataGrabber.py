from SoundPlayer import *
import threading

class PersonGrabber(threading.Thread):
    def __init__(self,soundManager):
        threading.Thread.__init__(self)
        self.started = False
        self.soundManager = soundManager
        self.dataPool = []
    def run(self):
        while True:
            if self.started:

                sound = Sound("Can you say your name : my name is Ziad Bougrine:","en",True,max)
                self.soundManager.addSound(sound)

                while not sound.played:
                    print(sound.played)
                text = recognize()
                print(text)
    def close(self):
        self.started = False
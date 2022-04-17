from SoundPlayer import *
import threading

class PersonGrabber(threading.Thread):
    def __init__(self,soundManager):
        threading.Thread.__init__(self)
        self.started = False
        self.soundManager = soundManager
    def run(self):
        while True:
            if self.started:
                self.soundManager.addSound(Sound("Can you say your name : my name is Ziad Bougrine:","en",True,True))
                while self.soundManager.isPlaying:
                    pass
                text = recognize()
                print(text)
    def close(self):
        self.started = False
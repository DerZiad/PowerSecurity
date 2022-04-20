from SoundPlayer import *

sound = Sound("hello","fr",False,0)
soundManager = SoundManager()
soundManager.start()
soundManager.addSound(sound)
while not sound.played:
    print(sound.played)
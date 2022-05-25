import SoundPlayer
from SoundPlayer import *

soundPlayer = SoundPlayer.SoundManager()
recognizerr = PowerRecognizer(soundPlayer)
recognizerr.recognize()
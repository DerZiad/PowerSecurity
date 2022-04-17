from Detector import *
from SoundPlayer import *
from PersonDataGrabber import *
import cv2
import datetime

def get_part_of_day(h):
    if 5 <= h <= 11:
        return "morning"
    elif 12 <= h <= 17:
        return "afternoon"
    elif 18 <= h <= 22:
        return "evening"
    else:
        return "night"
def checkIfFaceProcess(classNames):
    personNumber = 0
    for name in classNames:
        if name == "person":
            personNumber += 1
    return personNumber



startAlarm = False
processStarted = False

personDetector = PersonDetector('models/PersonDetector/mobilenet/saved_model', 'models/PersonDetector/mobilenet/coco.names')
faceDetector = FaceReconizer("models/FaceDetecter/haarcascade_frontalface_alt2.xml")

soundPlayer = SoundManager()
soundPlayer.start()

personGrabber = PersonGrabber(soundPlayer)
personGrabber.start()

capture = cv2.VideoCapture(0)
while True:
    now = datetime.datetime.now()
    isValable, frame = capture.read()
    if isValable:
        frame1 = frame.copy()
        frame, classNames = personDetector.createBoundingBox(frame)

        personNumber = checkIfFaceProcess(classNames)
        if personNumber > 1:
            soundPlayer.addSound(Sound("S'il vous plait, vous avez 1 minutes pour reculer ou l'alarme va démarrer","fr",False,max))
            startAlarm = True
            processStarted = False
            personGrabber.close()
        else:
            if personNumber == 1 and (not processStarted):
                soundPlayer.addSound(Sound("Starting face recognition","en",False,min))
                processStarted = True
                startAlarm = False
                personGrabber.started = True
        if processStarted:
            frame = faceDetector.createBoundingBox(frame,frame1)
        if get_part_of_day(now.hour) == "afternoon":
            frame[:, :, 0] = 0
            frame[:, :, 2] = 0
        cv2.imshow("Camera", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
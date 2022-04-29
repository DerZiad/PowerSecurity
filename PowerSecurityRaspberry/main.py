from Detector import *
from SoundPlayer import *
from PersonDataGrabber import *
import cv2

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
    isValable, frame = capture.read()
    if isValable:
        frame1 = frame.copy()
        frame, classNames = personDetector.createBoundingBox(frame)

        personNumber = checkIfFaceProcess(classNames)
        if personNumber > 1:
            soundPlayer.addSound(Sound("Please you should go back before 1 minute","en",False,max))
            startAlarm = True
            processStarted = False
            personGrabber.close()
        else:
            if personNumber == 1:
                if not processStarted:
                    soundPlayer.addSound(Sound("Starting face recognition","en",False,min))
                    processStarted = True
                    startAlarm = False
                    personGrabber.started = True
                else:
                    if personGrabber.name != "":
                        print("Detecting face")
                        frame = faceDetector.createBoundingBox(frame, frame1,personGrabber.name)
                    else:
                        faceDetector.i = 0
        cv2.imshow("Camera", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
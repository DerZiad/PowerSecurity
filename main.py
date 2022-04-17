from Detector import *
from SoundPlayer import *
import cv2
import datetime

personDetector = PersonDetector('models/PersonDetector/mobilenet/saved_model', 'models/PersonDetector/mobilenet/coco.names')
faceDetector = FaceReconizer("models/FaceDetecter/haarcascade_frontalface_alt2.xml")
def get_part_of_day(h):
    if 5 <= h <= 11:
        return "morning"
    elif 12 <= h <= 17:
        return "afternoon"
    elif 18 <= h <= 22:
        return  "evening"
    else:
        return "night"
def checkIfFaceProcess(classNames):
    personNumber = 0
    for name in classNames:
        if name == "person":
            personNumber += 1
    return personNumber


capture = cv2.VideoCapture(0)
startAlarm = False
processStarted = False
speecher = SoundManager()


while True:
    now = datetime.datetime.now()
    isValable, frame = capture.read()
    if isValable:
        frame1 = frame.copy()
        frame = personDetector.rescaleFrame(frame, scale=1)  # redimensionner l'image
        frame, classNames = personDetector.createBoundingBox(frame)
        personNumber = checkIfFaceProcess(classNames)

        if personNumber > 1:
            speecher.speech(text="S'il vous plait, vous avez 1 minutes pour se décaler ou l'alarme va démarrer",lang="fr",slow=False)
            startAlarm = True
            processStarted = False
        else:
            if personNumber == 1 and (not processStarted):
                speecher.speech(text="Demarrage de la reconnaissance faciale", lang="fr", slow=False)
                processStarted = True
                startAlarm = False

        if processStarted:
            frame = faceDetector.createBoundingBox(frame,frame1)
        if get_part_of_day(now.hour) == "evening":
            frame[:, :, 0] = 0
            frame[:, :, 2] = 0
        cv2.imshow("Camera", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
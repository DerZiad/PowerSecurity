from SoundPlayer import *
from PersonDataGrabber import *
import cv2
from ObjectScanner import *

def checkIfFaceProcess(classNames):
    personNumber = 0
    for name in classNames:
        if name == "person":
            personNumber += 1
    return personNumber



startAlarm = False
processStarted = False

objectScanner = ObjectScanner()

soundPlayer = SoundManager()
soundPlayer.start()

personGrabber = PersonGrabber(soundPlayer)
personGrabber.start()
detector = handDetector()
tipIds = [4, 8, 12, 16, 20]
capture = cv2.VideoCapture(0)

i = 0
while True:
    isValable, frame = capture.read()
    if isValable:
        frame1 = frame.copy()

        if not processStarted:
            img = detector.findHands(frame)
            lmList = detector.findPosition(frame)
            if len(lmList) != 0:
                fingers = []

                # Thumb
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # 4 Fingers
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # print(fingers)
                totalFingers = fingers.count(1)
                if totalFingers == 4:
                    processStarted = True
                    soundPlayer.addSound(Sound("Starting face recognition", "en", False, min))
                    soundPlayer.addSound(Sound("Taking multiple image of you", "en", False, max))
        else:
            frame, classNames = objectScanner.processObject(frame,['person'])
            personNumber = classNames['person']
            if personNumber > 1:
                soundPlayer.addSound(Sound("Process stoped, we can take only one person by one","en",False,max))
                processStarted = False
                personGrabber.close()
            elif personNumber == 1:
                frame,facesImage = objectScanner.processFace(frame, frame1)
                for face in facesImage:
                    savePath = "temporal" + "/" + str(i) + ".png"
                    cv2.imwrite(savePath, face)
                    if i == 20:
                        personGrabber.started = True
                        i = 0
                        break
                    i += 1
            else:
                processStarted = False
        cv2.imshow("Camera", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
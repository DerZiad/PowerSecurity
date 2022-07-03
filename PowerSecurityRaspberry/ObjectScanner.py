
import tensorflow as tf
import threading
import cv2
import numpy as np
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComplex = 1
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon,
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList

class ObjectScanner(threading.Thread):
    mobilenet = "models/PersonDetector/mobilenet/saved_model"
    classnames = "models/PersonDetector/mobilenet/coco.names"
    facedetector = "models/FaceDetecter/haarcascade_frontalface_alt2.xml"
    def __init__(self):
        self.loadModel()
        self.readClasses()
        self.loadModel()
    def loadModel(self):
        tf.keras.backend.clear_session()
        print("================>   Loading Object Scanner model ")
        self.objectDetectorModel = tf.keras.models.load_model(ObjectScanner.mobilenet)
        self.facedetectorModel = cv2.CascadeClassifier(ObjectScanner.facedetector)

    def readClasses(self):
        print("[ + ] - Reading classes")
        with open(ObjectScanner.classnames, 'r') as f:
            self.classesList = f.read().splitlines()
        self.colorList = np.random.uniform(low=0, high=255, size=(len(self.classesList), 3))

    def processFace(self, frame, frameFresh):
        gray = cv2.cvtColor(frameFresh, cv2.COLOR_RGB2GRAY)
        faces = self.facedetectorModel.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        facesImage = []
        for (x, y, w, h) in faces:
            roi_color = frame[y:y + h, x:x + w]
            facesImage.append(roi_color)
            color = (255, 0, 0)
            stroke = 1
            width = x + w
            heigth = y + h
            cv2.rectangle(frame, (x, y), (width, heigth), color, stroke)
        return frame,facesImage
    def processObject(self,image,names:list):
        inputTensorflow = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        inputTensorflow = tf.convert_to_tensor(inputTensorflow, dtype=tf.uint8)
        inputTensorflow = inputTensorflow[tf.newaxis, ...]

        detections = self.objectDetectorModel(inputTensorflow)
        bbox = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScores = detections['detection_scores'][0].numpy()
        imH, imW, imC = image.shape
        bboxIndx = tf.image.non_max_suppression(bbox, classScores, max_output_size=80, iou_threshold=0.5,
                                                score_threshold=0.7)
        classNames = {}
        for name in names:
            classNames[name] = 0
        if len(bboxIndx) != 0:
            for i in bboxIndx:
                classIndex = classIndexes[i]
                name = self.classesList[classIndex]
                for nameWanted in names:
                    if nameWanted == name:
                        classNames[nameWanted] += 1

                        bbox[i] = tuple(bbox[i])
                        classConfidence = round(100 * classScores[i])
                        classIndex = classIndexes[i]

                        classLabelText = self.classesList[classIndex]
                        classColor = self.colorList[classIndex]

                        displayText = '{} : {}%'.format(classLabelText, classConfidence)

                        ymin, xmin, ymax, xmax = bbox[i]

                        xmin, xmax, ymin, ymax = (xmin * imW, xmax * imW, ymin * imH, ymax * imH)
                        xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

                        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=classColor, thickness=1)
                        cv2.putText(image, displayText, (xmin, ymin - 10), cv2.FONT_HERSHEY_PLAIN, 1, classColor, 2)
        return image, classNames

'''capture = cv2.VideoCapture(0)
objectScanner = ObjectScanner()
pTime = 0
cTime = 0
detector = handDetector()
tipIds = [4, 8, 12, 16, 20]
while True:
    isValable, frame = capture.read()


    if isValable:
        frame, classNames = objectScanner.processObject(frame,['hat','eye glasses','person'])
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
            print(totalFingers)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Scanner",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()'''
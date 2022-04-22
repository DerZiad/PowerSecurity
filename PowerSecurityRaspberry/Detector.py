import numpy as np
import tensorflow as tf
import cv2
import warnings
warnings.filterwarnings("ignore")

class FaceReconizer:
    def __init__(self, modelPath):
        self.modelPath = modelPath
        self.loadModel()
        self.i = 0

    def loadModel(self):
        print("================>   Loading Face recognizer Model ")
        tf.keras.backend.clear_session()
        self.model = cv2.CascadeClassifier(self.modelPath)

    def createBoundingBox(self, frame,frameFresh,directory):
        gray = cv2.cvtColor(frameFresh, cv2.COLOR_RGB2GRAY)
        faces = self.model.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_color = frame[y:y + h, x:x + w]
            color = (255, 0, 0)
            stroke = 2
            width = x + w
            heigth = y + h
            savePath = directory + "/" + str(self.i) + ".png"
            cv2.imwrite(savePath, roi_color)
            cv2.rectangle(frame, (x, y), (width, heigth), color, stroke)
            self.i += 1
        return frame


class PersonDetector:
    def __init__(self, modelPath, classPath):
        self.disply_width = 640
        self.display_height = 480
        self.modelPath = modelPath
        self.classPath = classPath
        self.loadModel()
        self.readClasses()

    def rescaleFrame(self, frame, scale=0.75):
        width = int(frame.shape[1] * scale)
        heigth = int(frame.shape[0] * scale)
        dimension = (width, heigth)
        return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

    def readClasses(self):
        with open(self.classPath, 'r') as f:
            self.classesList = f.read().splitlines()
        self.colorList = np.random.uniform(low=0, high=255, size=(len(self.classesList), 3))

    def loadModel(self):
        print("================>   Loading Person detector Model ")
        tf.keras.backend.clear_session()
        self.model = tf.keras.models.load_model(self.modelPath)

    def createBoundingBox(self, image):
        inputTensorflow = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        inputTensorflow = tf.convert_to_tensor(inputTensorflow, dtype=tf.uint8)
        inputTensorflow = inputTensorflow[tf.newaxis, ...]

        detections = self.model(inputTensorflow)

        bbox = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScores = detections['detection_scores'][0].numpy()
        imH, imW, imC = image.shape
        bboxIndx = tf.image.non_max_suppression(bbox, classScores, max_output_size=50, iou_threshold=0.5,
                                                score_threshold=0.5)
        classNames = []
        if len(bboxIndx) != 0:
            for i in bboxIndx:
                classIndex = classIndexes[i]

                name = self.classesList[classIndex]
                if name == "person":
                    classNames.append(self.classesList[classIndex])

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

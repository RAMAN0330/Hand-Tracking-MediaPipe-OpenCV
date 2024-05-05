import cv2
import mediapipe as mp
import time

class handDetector:

    def __init__(self, mode=False, maxHands=2, complexity=1, detectionconf=0.5, trackconf=0.5):
        self.results = None
        self.mode = mode
        self.complexity = complexity
        self.maxHands = maxHands  # max number of hands can be detected
        self.detectionconf = detectionconf   # confidence interval for hand detection
        self.trackconf = trackconf  # confidence interval for tracking hand

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,
                                        self.maxHands,
                                        self.complexity,
                                        self.detectionconf,
                                        self.trackconf)  # For Detecting Hands
        self.mpDraw = mp.solutions.drawing_utils  # For drawing Points on hand

    def findHands(self, img, draw=True):
        # reading the image
        image_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting image from BGR format to RGB format
        self.results = self.hands.process(image_RGB)  # Passing images to mediapipe hand Detection to detect hands in it
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:  # detecting n number of hands
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms,
                                               self.mphands.HAND_CONNECTIONS)  # Drawing points and connection between them

        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []   # storing id and co-ordinates for landmark
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x+w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)   # pointing each point on the hands

        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)  # Capturing Video from laptop CAM as index is 0
    detector = handDetector()  # initializing Class handDetector
    while True:
        success, img = cap.read()
        img = detector.findHands(img)  # Finding hands on the video processed by cap.read()
        lmlist = detector.findPosition(img)   # finding Position of each point, on the hand
        if len(lmlist) != 0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)  # Calculating FPS of the video
        pTime = cTime

        cv2.putText(img,
                    str(int(fps)),
                    (10, 70),
                    cv2.FONT_HERSHEY_PLAIN,
                    3,
                    (255, 0, 255),
                    3)  # Putting it on the video at 10, 70
        cv2.imshow("Image", img)  # Displaying Video
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

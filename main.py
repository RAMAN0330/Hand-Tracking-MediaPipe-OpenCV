import cv2
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Capturing Video from laptop CAM as index is 0
detector = htm.handDetector()  # initializing Class handDetector
while True:
    success, img = cap.read()
    img = detector.findHands(img)  # Finding hands on the video processed by cap.read()
    lmlist = detector.findPosition(img)   # finding Position of each point, on the hand
    if len(lmlist) != 0:
        print(lmlist[8])

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
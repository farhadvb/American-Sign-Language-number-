# program American Sign Language(number)

import cv2
from cvzone.HandTrackingModule import HandDetector

wCam, hCam = 800, 600

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

detector = HandDetector(maxHands=1, detectionCon=0.8)

# To display the number in the image
numbers = ""

while True:
    success, img = cap.read()

    # Due to the rotation of the image, the thumb will be zero in the open position and one in the closed position.
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        if hands[0]['type'] == 'Right':
            fingers = []
            fingers = detector.fingersUp(hands[0])

            lmlist = hands[0]['lmList']
            
            #finger==['thumb','index finger','middle finger','ring finger','little finger']
            # thumb =  1 -> closed
            # thumb =0 -> open
            if lmlist[4][0] > lmlist[8][0] and fingers == [1, 0, 0, 0, 0]:  # all Fingers closed
                numbers = 0

            if fingers == [1, 1, 0, 0, 0]:  # index finger
                numbers = 1

            if fingers == [1, 1, 1, 0, 0]:  # index finger & middle finger
                numbers = 2

            if fingers == [0, 1, 1, 0, 0]:  # thumb & index finger & middle finger
                numbers = 3

            # index finger & middle finger & ring finger & little finger
            if fingers == [1, 1, 1, 1, 1]:
                numbers = 4

            if fingers == [0, 1, 1, 1, 1]:  # all fingers open
                numbers = 5

            if fingers == [1, 1, 1, 1, 0]:  # index finger & middle finger & ring finger
                numbers = 6

            if fingers == [1, 1, 1, 0, 1]:  # index finger & middle finger & little finger
                numbers = 7

            if fingers == [1, 1, 0, 1, 1]:  # index finger & ring finger & little finger
                numbers = 8

            if fingers == [1, 0, 1, 1, 1]:  # middle finger & ring finger & little finger
                numbers = 9

            if  lmlist[4][1]< lmlist[3][1] < lmlist[6][1]:  # thumb
                numbers = 10

            cv2.putText(img, f'number: {str(numbers)}', (10, 70), cv2.FONT_HERSHEY_PLAIN,
                        3, (255, 0, 0), 3)
            
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

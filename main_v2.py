import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random  


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
sttartGame = False
scores = [0,0]

while True:
    imgBG = cv2.imread("Resources/Group_1.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[40:360, 40:360] #cut imgScaled to 320x320
    #print("Dimensions of imgScaled:", imgScaled.shape)

    # find hands
    hands, img = detector.findHands(imgScaled, draw=True, flipType=True)

    if sttartGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (600, 400), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    #print("Number of fingers:", fingers)
                    if fingers ==[0,0,0,0,0]:
                        playerMove = 1
                    if fingers ==[1,1,1,1,1]:
                        playerMove = 2
                    if fingers ==[0,1,1,0,0]:
                        playerMove = 3

                    randomNumber =random.randint(1,3)
                    imgAI = cv2.imread(f"Resources/{randomNumber}.png",cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG,imgAI,(210,150))
                
                    # print(playerMove)
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1
                        print(scores[1] )

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1
                        


 
    imgBG[ 125:445,760:1080,:] = imgScaled  # merge  imgScaled in imgBg
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG,imgAI,(210,150))

    cv2.putText(imgBG, str(scores[0]), (443, 520), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 6)
    print(scores[0] )
    cv2.putText(imgBG, str(scores[1]), (1020, 520), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 6)
    print(scores[1] )


    #cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    #cv2.imshow("Scaled", imgScaled)

    key = cv2.waitKey(1)
    if key == ord('s'):
        # print("key",key)
        sttartGame = True
        initialTime = time.time()
        stateResult = False

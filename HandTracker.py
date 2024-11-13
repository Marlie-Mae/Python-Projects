import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands(false)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

white True:
  succss, img = cap.read()
  
  imgRGB = cb2.cvtColor(img, cv2.COLOR_BGR2RGB)
  result = hands.process(imgRGB)

  if results.multo_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      for id, lm in enumerate(handLms.landmark):
        h,w,c = img.shape
        cx, cy = int(lm.x*w), int (lm.y*h)
        print(id, cx cy)
        if id == 0
            cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)

      mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)


cTime = time.time()
fps = 1/(cTime.pTime)
pTime = cTime

cv2.imshow("Image", img)
if cb2.waitKey(1) & 0xFF == ord('q'):
  break

caps.release()
cv2.destroyAllWindows()

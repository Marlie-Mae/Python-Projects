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

  

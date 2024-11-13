import cv2
import mediapipe as mp
import time

def draw_landmarks(image, hand_landmarks):
  """Draws hand landmarks on the given image.

  Args:
    image: The input image in BGR format.
    hand_landmarks: A list of NormalizedLandmark objects representing the hand landmarks.
  """
  mp_drawing = mp.solutions.drawing_utils

  # Iterate through hands and draw landmarks
  for hand_landmarks in hand_landmarks:
    # Draw connections between landmark points
    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Optionally, highlight specific landmarks (e.g., wrist or fingertips)
    # for id, lm in enumerate(hand_landmarks.landmark):
    #   h, w, c = image.shape
    #   cx, cy = int(lm.x * w), int(lm.y * h)
    #   cv2.circle(image, (cx, cy), 5, (255, 0, 255), cv2.FILLED)  # Example: red circle for wrist

# Initialize MediaPipe hands solution with static image mode for processing images
mp_hands = mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

# Start video capture
cap = cv2.VideoCapture(0)

with mp_hands as hands:  # Ensure proper resource management with context manager
  while True:
    success, image = cap.read()

    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, you can check for the end of the file here
      continue

    # Convert image to RGB format, as MediaPipe expects RGB for processing
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect hand landmarks in the image
    results = hands.process(image_rgb)

    # Draw hand landmarks on the image if hands were detected
    if results.multi_hand_landmarks:
      draw_landmarks(image, results.multi_hand_landmarks)

    # Calculate frame rate
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    # Display the FPS and image with drawn landmarks
    cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Image', image)

    # Exit the loop on 'q' key press
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break

# Release resources
cap.release()
cv2.destroyAllWindows()

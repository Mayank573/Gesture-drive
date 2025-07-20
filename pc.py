import cv2
import mediapipe as mp
import socket

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Socket setup for communication
server_ip = '10.3.141.1'  # Raspberry Pi IP
port = 5000  # Port number  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Capture video feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe
    result = hands.process(rgb_frame)

    command = "stop"  # Default command

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example gestures:
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Gesture conditions:
            if thumb_tip.y < index_tip.y:  # Thumb up for "forward"
                command = "forward"
            elif thumb_tip.y > index_tip.y and pinky_tip.y > wrist.y:  # Palm down for "back"
                command = "back"
            elif thumb_tip.x < index_tip.x:  # Thumb to the left for "left"
                command = "left"
            elif thumb_tip.x > index_tip.x:  # Thumb to the right for "right"
                command = "right"

    # Send command to Raspberry Pi
    sock.sendto(command.encode(), (server_ip, port))

    # Display the frame
    cv2.putText(frame, f"Command: {command}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sock.close()

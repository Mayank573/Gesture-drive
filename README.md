# Hand Gesture Controlled RC Car

This project uses MediaPipe, OpenCV, and Python sockets to control an RC car using hand gestures captured through a webcam. Commands like `forward`, `back`, `left`, `right`, and `stop` are recognized and sent wirelessly to a Raspberry Pi, which drives the motors via an L298N motor driver.

---

## Tech Stack

- Python 3.11
- OpenCV (cv2) for video feed and visualization
- MediaPipe for real-time hand landmark detection
- Python UDP Sockets for communication
- Raspberry Pi 5 for motor control
- L298N Motor Driver
- GPIO for motor logic
- Windows (development PC)

---

## How It Works

1. MediaPipe tracks hand landmarks using your webcam.
2. Specific gestures (like thumb up or palm down) are mapped to movement commands.
3. The command is sent via UDP to the Raspberry Pi.
4. The Pi receives the command and moves the RC car accordingly.

---

Create and activate a virtual environment (Python 3.11):
py -3.11 -m venv .venv
.\.venv\Scripts\activate


Install dependencies:
pip install mediapipe opencv-python

On Raspberry Pi:
Install required GPIO library:
sudo apt update
sudo apt install python3-rpi.gpio

Connect the L298N motor driver to the correct GPIO pins.

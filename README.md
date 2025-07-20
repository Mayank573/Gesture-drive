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

## Gestures and Commands

| Gesture                  | Command Sent |
|--------------------------|--------------|
| Thumb up                 | forward      |
| Palm facing down         | back         |
| Thumb pointing left      | left         |
| Thumb pointing right     | right        |
| No hand detected / idle  | stop         |

---

## Installation and Setup

### On Development PC (Windows):

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gesture-rc-car.git
   cd gesture-rc-car

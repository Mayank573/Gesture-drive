import RPi.GPIO as GPIO
import socket
import time

# GPIO setup
ENA = 12
ENB = 13
IN1 = 5
IN2 = 6
IN3 = 20
IN4 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor pins setup
GPIO.setup([ENA, ENB, IN1, IN2, IN3, IN4], GPIO.OUT)
pwm1 = GPIO.PWM(ENA, 1000)
pwm2 = GPIO.PWM(ENB, 1000)
pwm1.start(100)
pwm2.start(100)

def move_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def move_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def turn_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def turn_right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# UDP socket setup
ip = "0.0.0.0"
port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

print("Waiting for commands...")

try:
    while True:
        data, _ = sock.recvfrom(1024)
        command = data.decode().strip()
        print(f"Received: {command}")

        if command == "forward":
            move_forward()
        elif command == "back":
            move_backward()
        elif command == "left":
            turn_left()
        elif command == "right":
            turn_right()
        else:
            stop()

except KeyboardInterrupt:
    print("Exiting...")

finally:
    stop()
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    sock.close()

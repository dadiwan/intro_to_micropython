from servo import Servo
import time

sg90_servo = Servo(pin=4)  #To be changed according to the pin used

while True:
    sg90_servo.move(0)  # turns the servo to 0°.
    time.sleep(1)
    sg90_servo.move(90)  # turns the servo to 90°.
    time.sleep(1)
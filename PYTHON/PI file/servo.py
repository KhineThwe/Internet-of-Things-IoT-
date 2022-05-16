import RPi.GPIO as GPIO
import time

servo_pin=5
duty_cycle=7.5  #should be the centre for a SERVO
#Configure the PI to use pin names (i.e.BCM) and allocate I/O
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
#Create PWM channel on the servo pin with a frequency of 50Hz
pwn_servo = GPIO.PWM(servo_pin,50)
pwn_servo.start(duty_cycle)

try:
   while True:
       duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Right = 10):"))
except KeyboardInterrupt:
       print("CRCL+C: Terminating program.")
finally:
       print("Cleaning up GPIO:....")
               
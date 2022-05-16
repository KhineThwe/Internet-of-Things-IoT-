import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
while True:
    data=int(input("Enter int1"))
    if data==1:
        GPIO.output(8,GPIO.HIGH)
        sleep(1)
        GPIO.output(10,GPIO.HIGH)
        sleep(1)
    else:
        GPIO.output(8,GPIO.LOW)
        sleep(1)
        GPIO.output(10,GPIO.LOW)
        sleep(1)
    #GPIO.output(10,GPIO.HIGH)
    #sleep(1)
    #GPIO.output(10,GPIO.LOW)
    #sleep(1)

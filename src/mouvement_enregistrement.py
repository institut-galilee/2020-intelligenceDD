import picamera
from time import sleep

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)


print ("Demarage")
try:
    time.sleep(2)

    while True:
        print("boucle")
        if GPIO.input(23):
            time.sleep(0.1)
            print ("Mouvement Detecte")
            #create object for PiCamera class
            camera = picamera.PiCamera()
            #set resolution
            camera.resolution = (1024, 768)
            camera.brightness = 60
            camera.start_preview()
            #add text on image
            camera.annotate_text = 'Hi AZIZ'
            time.sleep(1)
            #store image
            camera.capture('aziz.jpeg')
            camera.stop_preview()
        time.sleep(0.1)

except:
    GPIO.cleanup()
    print("clean")




#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

Button=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP) #action button

def action(Button):
 timer = 0
 while True:
  if (GPIO.input(Button) == False): 
   timer += 1 
  else:
   if (timer > 5):
    call(['sudo shutdown -h now'], shell=True)
   elif (timer > 2):
    call(['sudo shutdown -r now'], shell=True)
   timer = 0
  sleep(1)

GPIO.add_event_detect(Button,GPIO.FALLING,callback=action,bouncetime=200)

try:
 while True:
  sleep (2)

except KeyboardInterrupt:
 print ("Quit")
 GPIO.cleanup()       


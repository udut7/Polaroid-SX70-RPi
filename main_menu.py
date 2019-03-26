import time, os
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_SWITCH = 4
GPIO.setup(GPIO_SWITCH,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

Freq = 100
R = GPIO.PWM(16, Freq)
G = GPIO.PWM(20, Freq)
B = GPIO.PWM(21, Freq)

stateA = 0
stateB = 0

def kill(string):
 for line in os.popen("ps ax | grep " + string + " | grep -v grep"):
  fields = line.split()
  pid = fields[0]
  cmdp = 'sudo kill -9 ' + pid
  call ([cmdp], shell=True)

try:
 while True:
  while GPIO.input(GPIO_SWITCH) == 1:
   time.sleep(1)
  stateA = 1
  stateB = 0
  print ("photo to twitter")
  R.start(100)
  time.sleep(1)
  R.start(0)
  kill('restart_shutdown.py')
  cmd1 = 'python sx70_photo.py &'
  call ([cmd1], shell=True)
  while stateA == 1 and stateB == 0:
   if GPIO.input(GPIO_SWITCH) == 0:
    stateA = 1
    stateB = 1
    print ("video to twitter")
    G.start(100)
    time.sleep(1)
    G.start(0)
    kill('sx70_photo.py')
    cmd2 = 'python sx70_video_capture.py &'
    call ([cmd2], shell=True)
  while stateA == 1 and stateB == 1:
   if GPIO.input(GPIO_SWITCH) == 0:
    stateA = 0
    stateB = 1
    print ("future function")
    B.start(100)
    time.sleep(1)
    B.start(0)
    kill('sx70_video_capture.py')
    cmd3 = 'python future_function.py &'
    #call ([cmd3], shell=True)
  while stateA == 0 and stateB == 1:
   if GPIO.input(GPIO_SWITCH) == 0:
    stateA = 0
    stateB = 0
    print ("restart or shutdown")
    R.start(100)
    G.start(100)
    B.start(100)
    time.sleep(1)
    R.start(0)
    G.start(0)
    B.start(0)
    kill('future_function.py')
    cmd4 = 'python restart_shutdown.py &'
    call ([cmd4], shell=True)
    while GPIO.input(GPIO_SWITCH) == 0:
     time.sleep(0.1)
    time.sleep(0.1)
 
except KeyboardInterrupt:
 print ("Quit")
 GPIO.cleanup() 
GPIO.cleanup()

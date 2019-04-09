import picamera
import datetime
import time, os
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_SWITCH = 12
GPIO.setup(GPIO_SWITCH,GPIO.IN,pull_up_down = GPIO.PUD_UP)

print ("  Press Ctrl & C to Quit")

Record = 0

try:
   while True:
      with picamera.PiCamera() as camera:
         camera.resolution = (700, 700)
         camera.framerate = 25
         while GPIO.input(GPIO_SWITCH) == 1 :
            time.sleep(0.25)
         Record = 1
         print ("Recording")
         now = datetime.datetime.now()
         timestamp = now.strftime("%y%m%d%H%M%S")
         video_path = '/home/pi/movie/capture/'
         camera.start_preview()
         camera.start_recording(video_path + timestamp + '.h264')
         time.sleep(.5)
         while Record == 1:
            camera.wait_recording(.01)
            if GPIO.input(GPIO_SWITCH) == 0:
               print ("Stopped")
               camera.stop_recording()
               Record = 0
               while GPIO.input(GPIO_SWITCH) == 0:
                  time.sleep(0.1)
               time.sleep(.5)
      cmd = 'MP4Box -add ' + video_path + timestamp + '.h264 ' + video_path + timestamp + '.mp4'
      call ([cmd], shell=True)
      os.remove(video_path + timestamp + '.h264')
      os.rename(video_path + timestamp + '.mp4', '/home/pi/movie/edit/' + timestamp + '.mp4')
 
except KeyboardInterrupt:
  print ("Quit")
  GPIO.cleanup() 

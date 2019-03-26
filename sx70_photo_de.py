#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import tweepy, os, time, picamera, pygame, io, sys 
from PIL import Image
from pygame.locals import *
from subprocess import call  
from datetime import datetime  
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #shutter button

Freq = 100
R = GPIO.PWM(16, Freq)
G = GPIO.PWM(20, Freq)
B = GPIO.PWM(21, Freq)
os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()
screen = pygame.display.set_mode((160, 124), 0, 32)
screen.fill(0)
clock = pygame.time.Clock()

font1 = pygame.font.SysFont(None, 20)
text1 = font1.render('@SX70_RPi', True, (255, 165, 0))
text1 = pygame.transform.rotate(text1, 90)
screen.blit(text1, (110, 25))

font2 = pygame.font.SysFont(None, 13)
text2 = font2.render('by your name', True, (255, 165, 0))
text2 = pygame.transform.rotate(text2, 90)
screen.blit(text2, (145, 25))

width = 704
height = 704
rgb_buffer = bytearray(width * height * 3)
camera = picamera.PiCamera()
camera.resolution = (width, height)
offset = 22

for i in range(5):
 B.start(100)
 sleep(0.3)
 B.start(0)
 sleep(0.1)

de_path = '/home/pi/double_exposure/'

try:
 while True:
  exposure = 1
  while exposure < 3:
   while GPIO.input(18):
    font3 = pygame.font.SysFont(None, 16)
    clock.tick(1)
    theTime=time.strftime("%H:%M:%S", time.localtime())
    text3=font3.render(str(theTime), True,(255,165,0),(0,0,0))
    text3 = pygame.transform.rotate(text3, 90)
    screen.blit(text3, (80,25)) 
    stream = io.BytesIO()
    camera.capture(stream, format='rgb')
    stream.seek(0)
    stream.readinto(rgb_buffer)
    stream.close()
    img = pygame.image.frombuffer(rgb_buffer, (width, height), 'RGB')
    img = pygame.transform.scale(img, (int(img.get_width() * 80 / img.get_height()), 80))
    img = pygame.transform.rotate(img, 90) 
    screen.blit(img, (0, offset))
    pygame.display.update() 

   R.start(100)
   sleep(0.3)
   R.start(0)  
   sleep(0.1)
   R.start(100)

   exp_name = 'exposure_' + str(exposure) + '.jpg'  
   camera.capture(de_path + exp_name)
   exposure = exposure + 1
   R.start(0)
  
  R.start(100) 
  i = datetime.now()               
  now = i.strftime('%Y%m%d-%H%M%S')  
  mark_date = i.strftime('%Y/%m/%d %H:%M') 
  photo_name = now + '.jpg'
  image1 = Image.open(de_path + 'exposure_1.jpg')
  image2 = Image.open(de_path + 'exposure_2.jpg')
  image3 = image1.convert("RGBA")
  image4 = image2.convert("RGBA")
  image5 = Image.blend(image3, image4, alpha=0.3)
  image6 = image5.convert("RGB")
  image6.save(de_path + photo_name)
  cmd = 'python polaroid.py ' + de_path + photo_name + ' center "@SX70_RPi - ' + mark_date + '"'
  call ([cmd], shell=True)
  preview = pygame.image.load(de_path + photo_name)
  preview = pygame.transform.scale(preview, (int(img.get_width() * 80 / img.get_height()), 80))
  preview = pygame.transform.rotate(preview, 90)
  screen.blit(preview,(0, offset))
  pygame.display.flip()
  sleep(1)

  R.start(0)
  sleep(0.5)

  consumer_key = 'your consumer_key'  
  consumer_secret = 'your consumer_secret'  
  access_token = 'your access_token'  
  access_token_secret = 'your access_token_secret'  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)  
  api = tweepy.API(auth)  
  photo_path = de_path + photo_name  
  status = 'Photo auto-tweet from Polaroid SX-70 #polaroid #sx70 #raspberrypi #double_exposure'

  G.start(100)
  sleep(0.3)
  G.start(0)
  sleep(0.1)
  G.start(100)

  api.update_with_media(photo_path, status=status)  
  os.remove(de_path + 'exposure_1.jpg')
  os.remove(de_path + 'exposure_2.jpg')
  os.remove(photo_path)
  
  G.start(0)
  sleep(0.5)

except KeyboardInterrupt:
 print ("Quit")
 GPIO.cleanup()
 pygame.quit()
 sys.exit()


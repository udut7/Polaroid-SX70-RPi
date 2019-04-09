import os
import tweepy
from datetime import datetime
from subprocess import call

for root, dir, files in os.walk("./movie/upload/"):
 for filename in files:
  i = datetime.now()               
  upload_path = '/home/pi/movie/upload/'
  consumer_key = 'your consumer_key'  
  consumer_secret = 'your consumer_secret'  
  access_token = 'your access_token'  
  access_token_secret = 'your access_token_secret'  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
  auth.set_access_token(access_token, access_token_secret)  
  api = tweepy.API(auth)  
  status = 'Video auto-tweet from Polaroid SX-70 #polaroid #sx70 #raspberrypi'
  upload_result = api.media_upload(upload_path + filename)
  api.update_status(status=status, media_ids=[upload_result.media_id_string])
  os.remove(upload_path + filename)


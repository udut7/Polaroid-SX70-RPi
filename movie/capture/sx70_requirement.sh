#!/bin/bash
sudo apt-get update
sudo apt-get install python-pip -y
sudo apt-get install git -y
sudo pip install picamera
sudo apt-get install python-pygame -y
sudo apt-get install libjpeg8-dev -y
sudo pip install Pillow
git clone https://github.com/udut7/tweepy.git
cd tweepy
sudo python setup.py install


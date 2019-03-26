Polaroid SX-70 camera using Raspberry Pi Zero W python project, auto upload photo double exposure and video polaroid style with time and date variables to twitter at https://twitter.com/SX70_RPi

Hardware:
- Polaroid SX-70
- Raspberry Pi Zero W
- Raspberry Pi Camera
- 0.96 inch (80x160) TFT display 65K full color SPI (GPIO3, GPIO10, GPIO11, GPIO22 & GPIO27)
- RGB led for light indicator replace film counter (GPIO16, GPIO20 & GPIO21)
- DC Stepper Motor Drive Controller
- Power Module Lithium Battery
- Capacitive Touch Key Switch Module for main menu loop selection button (GPIO4):
    1. Photo to twitter (red blink indicator)
    2. Video to twitter (green blink indicator)
    3. Double Exposure Photo to twitter (blue blink indicator)
    4. Restart or Shutdown (white blink indicator)
- Original SX-70 shutter button for action loop button of each menu selected (GPIO18):
    1. Action at Photo to twitter menu:
         - Take photo (red light for take photo continued with green light for upload to twitter)
    2. Action at Video to twitter menu:
         - Start Recording (red light start record)
         - Stop Recording (red light stop record continued with green light for upload to twitter)
    3. Action at Double Exposure Photo to twitter menu:
         - Take first main photo (red light for take photo)
         - Take second transparant photo (red light for take photo continued with green light for upload to twitter)
    4. Action at Restart or Shutdown menu (red light timer):  
         - Short pressed, between 2 until 5 seconds: restart
         - Long pressed, above 5 seconds: shutdown

Operating System:
- Raspbian Stretch Lite

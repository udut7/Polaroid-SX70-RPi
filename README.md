Polaroid SX-70 camera using Raspberry Pi Zero W python project, auto upload photo and video polaroid style with time and date variables to twitter at https://twitter.com/SX70_RPi

Hardware:
- Polaroid SX-70
- Raspberry Pi Zero W
- Raspberry Pi Camera
- 0.96 inch (80x160) TFT display 65K full color SPI (GPIO3, GPIO10, GPIO11, GPIO22 & GPIO27)
- RGB led for light indicator replace film counter (GPIO16, GPIO20 & GPIO21)
- DC Stepper Motor Drive Controller
- Power Module Lithium Battery
- Capacitive Touch Key Switch Module for main menu selection button (GPIO4):
    1. Photo to twitter (red blink indicator)
    2. Video to twitter (green blink indicator)
    3. Future function (blue blink indicator)
    4. Restart or Shutdown (white blink indicator)
- Original SX-70 shutter button for action button of each menu selected (GPIO18):
    1. Action at Photo to twitter menu:
         - Take photo (red light for take photo, green light for upload to twitter)
    2. Action at Video to twitter menu:
         - Start Recording (red light for video record, green light for upload to twitter)
         - Stop Recording
    3. Future function
    4. Action at Restart or Shutdown menu:
         - Short pressed: restart
         - Long pressed: shutdown

Operating System:
- Raspbian Stretch Lite

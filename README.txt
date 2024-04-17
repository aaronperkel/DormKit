______                     _   ___ _   
|  _  \                   | | / (_) |  
| | | |___  _ __ _ __ ___ | |/ / _| |_ 
| | | / _ \| '__| '_ ` _ \|    \| | __|
| |/ / (_) | |  | | | | | | |\  \ | |_ 
|___/ \___/|_|  |_| |_| |_\_| \_/_|\__|
                                       
Version 1.0 - 12/06/23 14:22
Created by: Owen Cook, Alexa Witkin, Sam Zimpfer, Aaron Perkel
=============================================================================================

== Description == 

DormKit is a prototype "smart dorm" product that allows a user to install some hardware in their dorm
to control certain electronics from anywhere on UVM campus. The name was picked because of the popular
smart home framework made by Apple: "HomeKit". It is still definitely a work in progress, but we are
happy to present V1.0.

DormKit works using a Flask web app. The control signals from the web are sent over WiFi to the Raspberry Pi. 
It also has a "hub" that stays in the dorm that shows other relevant information. This is connected directly
to the Pi. The Pi then sends signals over Bluetooth to control the peripherals using an Arduino Uno.

== File Structure ==

.
├── static/
│   ├── styles.css
│   └── buttons.js
├── templates/
│   └── buttons.html
├── textures/
│   ├── button.png
│   ├── door.png
│   ├── font.ttf
│   ├── light.png
│   ├── off.png
│   └── on.png
├── main.py
├── main.sh
├── HC_05.py
├── app.py
├── hub.py
├── HC-05.ino
└── states.txt

== LCD Setup ==

To set up the LCD Screen with a Raspberry Pi, please follow the instructions in its documentation
https://www.waveshare.com/wiki/5inch_HDMI_LCD

== How to Use DormKit == 

1. Please ensure you have the following version or greater of python installed
	- Python 3.10.2

2. Please ensure you have the following python libraries installed with INDICATED VERSION OR GREATER
	- pygame 2.1.2
	- geocoder 1.38.1
	- geopy 2.4.0
	- requests 2.28.1
	- smbus 1.1.post2

3. Please ensure you have the following libraries installed on your Raspberry Pi
	- libsdl2-image2.0-0
	- libsdl2-ttf-2.0-0

3. Make sure the Arduino Uno AND the Raspberry Pi are plugged into power

4. Build and run main.py from the Raspberry Pi HUB

5. Controls are accessed through the HUB or through the Pi's IP address

== NOTES ==

DormKit WILL NOT RUN OR COMPILE if not ran on a raspberry pi using the steps above. If you 
would like to run hub.py on something that is not a raspberry pi, please
COMMENT OUT LINES:
	- 9
	- 20
	- 21
	- 106
	- 136
	- 190
AND UNCOMMENT LINES:
	- 109

The API KEY for the weather on line 71 has been [REDACTED]


'''
Hub V1.2 12/06/23 11:12
hub.py
DORMKIT V1.0
'''

# Syncing the bluetooth
import subprocess as sp
sp.run('sudo rfcomm bind 2 98:D3:61:F7:14:36', shell=True)

# Make sure these libraries are installed
import pygame as pg
import sys
import geocoder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import time
from io import BytesIO
import HC_05 as control
import smbus


'''
The class for the buttons
(currently just black circles)
'''
class Button:
    global screen
    def __init__(self, xLoc, yLoc, button_number):
        self.xLoc = xLoc # location of button on screen
        self.yLoc = yLoc
        self.button_number = button_number
        self.on = pg.transform.scale(pg.image.load('textures/on.png'), (60, 60))
        self.off = pg.transform.scale(pg.image.load('textures/off.png'), (60, 60))

    
    def draw(self):
        # draws button on screen, black, location, radius of 25
        pg.draw.circle(screen, (255, 255, 255), (self.xLoc, self.yLoc), 30)
        if self.button_number in [0, 2]:
            screen.blit(self.on, (self.xLoc - 30, self.yLoc - 30))
        else:
            screen.blit(self.off, (self.xLoc - 30, self.yLoc - 30))

    def click(self):
        mouseX, mouseY = pg.mouse.get_pos()
        # if mouse clicks inside button
        if self.xLoc + 12 >= mouseX >= self.xLoc - 12:
            if self.yLoc + 12 >= mouseY >= self.yLoc - 12:
                # assigns correct function to each button
                if self.button_number == 0:
                    control.lock_door()
                elif self.button_number == 1:
                    control.unlock_door()
                elif self.button_number == 2:
                    control.light_on()
                elif self.button_number == 3:
                    control.light_off()

'''
Grabs weather using the API i found online
this happens every 2 minutes
'''
def get_new_weather():
    global start_time, temp, condition, high, low, icon, weather1, weather2, img
    start_time = time.time() # resets timer
    # url is made based on location of pi currenlty
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(
    g.latlng[0]) + '&lon=' + str(
        g.latlng[1]) + '&APPID=[REDACTED]&units=imperial'
    response = requests.get(url)
    x = response.json()
    # gets the weather icon
    icon = 'https://openweathermap.org/img/wn/' + x['weather'][0]['icon'] + '@2x.png'
    response = requests.get(icon)
    img = pg.image.load(BytesIO(response.content)) # loads weather icon
    # temperature
    temp = int(x['main']['temp'])
    # condition
    condition = x['weather'][0]['description'].title()
    # temp high
    high = int(x['main']['temp_max'])
    # temp low
    low = int(x['main']['temp_min'])
    # creates the 2 lines of weather
    weather1 = title2.render(f'{temp}º, {condition}', True, 0)
    weather2 = title2.render(f'H:{high}º L:{low}º', True, 0)

def get_temperature():
    global roomTemp
    BUS = smbus.SMBus(1)
    ADDRESS = 0x48
    rvalue0 = BUS.read_word_data(ADDRESS,0)
    rvalue1 = (rvalue0 & 0xff00) >> 8
    rvalue2 = rvalue0 & 0x00ff
    rvalue = (((rvalue2 * 256) + rvalue1) >> 4 ) * .0625
    roomTemp = title2.render(f"Room Temp: {round((rvalue * (9/5)) + 32, 2)}º", True, 0)

# tuples
screenW, screenH = 800, 480
screen_size = (screenW, screenH)
background_color = (146, 132, 176)

# screen FOR raspberry pi
screen = pg.display.set_mode(screen_size, pg.FULLSCREEN)

# screen NOT FOR raspberry pi
# screen = pg.displat.set_mode(screen_size)

# pygame setup
pg.init()
pg.display.set_caption('Hub')
start_time = time.time()
bckgrnd = pg.transform.scale(pg.image.load('textures/button.png'), (250, 275))
light = pg.transform.scale(pg.image.load('textures/light.png'), (185, 185))
door = pg.transform.scale(pg.image.load('textures/door.png'), (165, 165))

# location and weather setup
g = geocoder.ip('me')
geolocator = Nominatim(user_agent="hub")
location = geolocator.reverse((g.latlng[0], g.latlng[1]))
city = str(location).split(', ')[4]
state = str(location).split(', ')[-3]

# font classes
title1 = pg.font.Font('textures/font.ttf', 72)
title2 = pg.font.Font('textures/font.ttf', 24)

# text renders
dorm = title1.render('UHS T2 359', True, 0)
location = title2.render(city + ', ' + state, True, 0)
roomTemp = title2.render("Room Temp:", True, 0)

# gets weather and adds 4 buttons to a list
get_temperature()
get_new_weather()
click = False
buttons = []
buttons.append(Button(165, 375, 0))
buttons.append(Button(273, 375, 1))
buttons.append(Button(165 + 325, 375, 2))
buttons.append(Button(273 + 325, 375, 3))

# pygame loop
while True:
    screen.fill(background_color)
    now = datetime.now() # current time
    # time/date formatting
    date = title2.render(now.strftime("%A, %B %d, %Y"), True, 0)
    curr_time = title2.render(now.strftime("%I:%M:%S %p"), True, 0)
    
    for event in pg.event.get():
        # if the 'x' is clicked in the window
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # if the mouse is clicked
        if event.type == pg.MOUSEBUTTONDOWN:
            click = True

    # draws text
    screen.blit(dorm, (5, 5))
    screen.blit(location, (5, dorm.get_height() - 10))
    screen.blit(date, (screenW - date.get_width() - 5, 5))
    screen.blit(curr_time, (screenW - curr_time.get_width() - 5, date.get_height() + 5))
    screen.blit(weather1, (5, dorm.get_height() + 15))
    screen.blit(weather2, (5, dorm.get_height() + 40))
    screen.blit(img, (200, 35))
    screen.blit(bckgrnd, (100, 175))
    screen.blit(bckgrnd, (425, 175))
    screen.blit(door, (125, 190))
    screen.blit(light, (450, 180))
    screen.blit(roomTemp, (screenW - roomTemp.get_width() - 5, date.get_height() + curr_time.get_height() + 5))
    

    # draws buttons
    for button in buttons:
        button.draw()

    # if the user clicks
    if click:
        for button in buttons:
            button.click()
            click = False
        
    # gets new weather every 2 minutes
    if (time.time() - start_time >= 120):
        get_temperature()
        get_new_weather()

    # refresh display
    pg.display.update()

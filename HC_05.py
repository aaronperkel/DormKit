'''
HC_05.py
DORMKIT V1.0
'''

import serial
import time

bluetooth = serial.Serial("/dev/rfcomm2", 9600) # send serial value

lightState = ''
doorState = ''

def getDoorState():
    return doorState

def getLightState():
    return lightState
# sets lightState and doorState variables to their approriate values, depending on the current state of the light and door servos
def loadCurrentStates():
    with open('states.txt') as file:
        lines = []
        for line in file:
            lines.append(line)
        
        global lightState, doorState
        lightState = lines[0]
        doorState = lines[1]
        
        print("LIGHT STATE: " + lightState)
        print("DOOR STATE: " + doorState)

loadCurrentStates()

# updates state file to hold current values of lightState and doorState variables
def updateStates():
    with open('states.txt', 'w') as file:
        file.write(lightState)
        file.write(doorState)
        
    print("UPDATED LIGHT STATE: " + lightState)
    print("UPDATED DOOR STATE: " + doorState)

# Sends a serial code 'a' to Arduino    
def send_bluetooth_data(a):
    string = 'X{0}'.format(a) # format of our data
    print('Serial code:' + string)
    bluetooth.write(string.encode("utf-8"))
    
    updateStates()
    
def led_on():
    send_bluetooth_data(100)
    
def led_off():
    send_bluetooth_data(200)
    
def light_on():
    global lightState
    if lightState == 'off\n':
        lightState = 'on\n'
        send_bluetooth_data(300)
    
def light_off():
    global lightState
    if lightState == 'on\n':
        lightState = 'off\n'
        send_bluetooth_data(400)
    
def lock_door():
    global doorState
    if doorState == 'unlocked\n':
        doorState = 'locked\n'
        send_bluetooth_data(500)
    
def unlock_door():
    global doorState
    if doorState == 'locked\n':
        doorState = 'unlocked\n'
        send_bluetooth_data(600)

# main loop for testing only
if __name__ == "__main__":
    while True:
        a = input("enter: -") # input value to be received by arduino bluetooth
        ''' this is where we can determine what pins we want on to control each
        component independently '''
    
        send_bluetooth_data(a)

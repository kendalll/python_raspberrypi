#!/usr/bin/env python
import cayenne.client

# Servo Control
import time
import wiringpi
import os
import sys

#error trap when you're not root before configuring GPIO
if not os.geteuid() == 0: 
	sys.exit("\nError!\n***Run this script as root or you're gonna have a bad time***\n")

    
    
    
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

def servo_move():
    for loops in range (1, 2, 1):
        for pulse in range(152, 132, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(132, 152, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
    print "\nWater is heating!"


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "ace55b60-8511-11e7-9727-55550d1a07e7"
MQTT_PASSWORD  = "373de1ee07e33df0ba1f1637c2ab39e2a386a229"
MQTT_CLIENT_ID = "baca0200-8523-11e7-a491-d751ec027e48"


# The callback for when a message is received from Cayenne.
def on_message(message):
    servo_move()
    # print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.


client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
client.loop_forever()















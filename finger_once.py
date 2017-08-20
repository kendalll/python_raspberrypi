
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

for loops in range (1, 2, 1):
        for pulse in range(152, 132, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(132, 152, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
print "\nservo ran: %s loops\n" %loops 
sys.exit()

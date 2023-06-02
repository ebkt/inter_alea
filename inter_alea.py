# inter alea 
# ebkt 2023

import time # time library for sleep timer 
import board # import board info
from adafruit_motorkit import MotorKit
import random # random library

kit = MotorKit(i2c=board.I2C()) #create kit variable
order = [kit.motor1, kit.motor2, kit.motor3, kit.motor4] # store each motor in an array so we can randomise the order

sleep1 = 0.5 # period for how long solenoids will be ON
sleep2 = 0.5 # period for how long solenoids will be OFF

# randomisation function
def randomise():
    print("changing sleep time")                            # tell us what's happening
    _sleep1 = random.random()                               # new variable _sleep1 to avoid using globals, will be returned and used as sleep1
    _sleep2 = random.random()                               # same for _sleep2
    _order = sorted(order, key = lambda _: random.random()) # reorder the array of solenoids
    print(_order)                                           # print the new array order
    return _sleep1, _sleep2, _order                         # return the two sleep values and new array


while True:
    for i in range(len(order)):                 # loop through however many motors we have in the order array
        order[i].throttle = 1.0                 # each time through the for loop, check which motor is currently stored at that index in order[] and fire it
        time.sleep(sleep1)                      # rest sleep1 (motor is on)
        order[i].throttle = 0                   # turn this motor off
        time.sleep(sleep2)                      # rest sleep2 (motor is off)
        # do the above for all 4 motors
        # if we're at the end of the for loop/array, randomly decide whether to randomise and all sleep for a bit
        if i==len(order)-1 and random.random() < 0.3:
            print("sleeping")                   # tell us the motors are sleeping
            sleep1, sleep2, order = randomise() # adjust variables (this line only works because the function returns 3 values)
            time.sleep(random.randint(1, 10))   # now all motors sleep
#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase



left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)
# Initialize a sensor
sensor = UltrasonicSensor(Port.S4)
# Drive forward until an object is detected
robot.drive(100, 0)
while sensor.distance() > 500:
wait(10)
robot.stop()

###########
# initialize the color sensors
#motor_a = Motor(Port.A)
#motor_b = Motor(Port.B)

#ColorSensorLeft = ColorSensor(Port.1)
#ColorSensorRight = ColorSensor(Port.2)

## the sudo 
# 1. If the left one sees a line, backup and turn right.
# 2. If the right one sees a line, backup and turn left.
# 3. Otherwise go forward.

#for loop

#if ColorSensorLeft = low:

#elif ColorSensorRight = low:
#    right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

#else:

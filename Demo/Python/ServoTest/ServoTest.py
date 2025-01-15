#!/usr/bin/python

from Emakefun_MotorHAT import Emakefun_MotorHAT, Emakefun_Servo
import time
mh = Emakefun_MotorHAT(addr=0x60)

myServo = mh.getServo(1)
while (True):

    myServo.writeServo(180)
    time.sleep(2)
    myServo.writeServo(0)
    time.sleep(2)


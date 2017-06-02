#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)

while True:
  if (GPIO.input(27)):
    os.system("poweroff")
    break
  time.sleep(1)

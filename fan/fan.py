#!/usr/bin/env python3

import os
import time
from time import sleep
import signal
import sys
import RPi.GPIO as gpio

MAX_TEMP = float(os.getenv('MAX_TEMP', 65))
MIN_TEMP = float(os.getenv('MIN_TEMP', 45))

FAN_GPIO = int(os.getenv('FAN_GPIO', 18))
FAN_MIN = int(os.getenv('FAN_MIN', 0))
FAN_MAX = int(os.getenv('FAN_MAX', 100))
FAN_FREQ = int(os.getenv('FAN_FREQ', 17))

INTERVAL = int(os.getenv('INTERVAL', 5))
PRINT_LOG = bool(os.getenv('PRINT_LOG', True))

def init_pwm():
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)
  gpio.setup(FAN_GPIO, gpio.OUT)
  pwm = gpio.PWM(FAN_GPIO, FAN_FREQ)
  pwm.start(50)
  gpio.setwarnings(False)
  return pwm

def get_cpu_temp():
    temp = os.popen('cat /sys/class/thermal/thermal_zone*/temp').readline()
    temp = float(temp)
    temp /= 1000.0
    return temp

def set_fan_speed(pwm, speed, temp):
  pwm.ChangeDutyCycle(speed)
  
  if PRINT_LOG:
    print("cpu temperature: %4.2f, fan speed: %5d" % (temp, speed))

def handle_fan(pwm):
  temp = get_cpu_temp()

  # Turn off the fan if temperature is below MIN_TEMP
  if temp < MIN_TEMP:
      set_fan_speed(pwm, FAN_MIN, temp)
  # Set fan speed to MAXIMUM if the temperature is above MAX_TEMP
  elif temp > MAX_TEMP:
      set_fan_speed(pwm, FAN_MAX, temp)
  # Caculate dynamic fan speed
  else:
      step = (FAN_MAX - FAN_MIN)/(MAX_TEMP - MIN_TEMP)   
      delta = temp - MIN_TEMP
      speed = FAN_MIN + (round(delta) * step)
      set_fan_speed(pwm, speed, temp)

try:
    pwm = init_pwm()
    set_fan_speed(pwm, 0, get_cpu_temp())
    while True:
        handle_fan(pwm)
        sleep(INTERVAL)
except KeyboardInterrupt:
    set_fan_speed(pwm, 0, get_cpu_temp())
finally:
    gpio.cleanup()

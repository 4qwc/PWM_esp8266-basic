# PWM basic
from machine import Pin, PWM  # กำหนด เพิ่ม PWM
import math
import time

FRQ = 5000
led_2 = PWM(Pin(5), FRQ)
while True:
  for duty_cycle in range(0, 1024):
    led.duty(duty_cycle)
    time.sleep(0.005)

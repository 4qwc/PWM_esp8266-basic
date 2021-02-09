# *****************************
# -------  *** การใช้งาน  PWM

from machine import Pin, PWM  # กำหนด เพิ่ม PWM
import math
import time


led = PWM(Pin(4), freq=1000, duty=0) # pin output 5
# กำหนด output pin 4/ ความถี่, ดิวตี้
def pulse(ld, t):
    for i in range(20):
        ld.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:
    pulse(led, 50)
    time.sleep(1)
    for i in range(3): # กระพริบ 3 ครั้ง
        pulse(led, 20)

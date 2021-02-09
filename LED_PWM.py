# PWM basic
# การใช้งาน PWM ปรับไฟ หรี่ไฟ
from machine import Pin, PWM  # กำหนด เพิ่ม PWM
import math
import time

FRQ = 100
led1 = PWM(Pin(5), FRQ)


def L1():
    for i in range(1024, 0, -1):# 1024=จุดเริ่มต้น/# 0= ค่าสิ้นสุด/-1=เปลี่ยนค่ารอบละ-1
        led1.duty(i)
        time.sleep_ms(2)

    for t in range(0, 1024, 1): # 0 = จุดเริ่มต้น/# 1024 = ค่าสิ้นสุด/1=เปลี่ยนค่ารอบละ1
        led1.duty(t)
        time.sleep_ms(2)


while True:
    L1()




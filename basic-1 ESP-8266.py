# ESP 8266

from machine import Pin  # กำหนด GPIO pin
import time

led = Pin(16, Pin.OUT)  # กำหนด output pin
l =   Pin(2, Pin.OUT)
l.on()
"""
   Pin.IN  อ่านข้อมูลเข้า
   Pin.OUT เขียนข้อมูล output
   Pin.OPEN_DRAIN  output แบบ open drain
   Pin.ALT โหมดส่วนเสริมใช้เฉพาะขาที่รองรับเท่านั้น
   Pin.ALT_OPEN_DRAIN  โหมดส่วนเสริมใช้เฉพาะขาที่รองรับเท่านั้นและเพิ่ม
   output แบบ open drain

   การใช้ Pin.mode(Pin.IN)
#--------------------------------#
   นอกจากนี้ยังมี method Pin.pull[pull]
        Pin.PULL_UP
        Pin.PULL_DOWN
    Example: Pin.pull(Pin.PULL_UP)
#--------------------------------#
    Method Pin.drive([])
        Pin.LOW_POWER
        Pin.MID_POWER
        Pin.HIGH_POWER
     Example: Pin.drive(Pin.HIGH_POWER)
#--------------------------------#

"""
# Pin.on()# กำหนดเป็น ON
# Pin.off()# กำหนด

"""
i = 0
while i<100:
    i+=1
    if i >50:
        led.on()
        print('LED_OFF')
        break
    #led.value(0)
    led.on()

    print('LED ON', i)
    print('......')
    time.sleep_ms(100)
    #led.value(1)

    led.off()
    print('LED..... OFF', i)
    print('......')
    time.sleep_ms(100)
"""

# ------------------------------ While

T_ms = [1000, 500, 250, 100, 50]
r = 0
while True:
    for i in range(0, 4):
        led.off()
        print("LED OFF")
        time.sleep_ms(T_ms[r])  # ดึงค่ามาจาก >T_ms /r=กำหนดรอบ
        led.on()
        print("LED ON")
        time.sleep_ms(T_ms[r])
    r = r + 1
    if r > 4:
        r = 0

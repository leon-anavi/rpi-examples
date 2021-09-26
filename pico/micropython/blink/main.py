import time
from machine import Pin
led = Pin(25, Pin.OUT)
while True:
    led.toggle()
    time.sleep(1) 
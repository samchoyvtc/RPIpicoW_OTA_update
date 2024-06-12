from machine import Pin
import time
import ugit
wlan = ugit.wificonnect()
led_pin  = Pin(28, Pin.OUT)

for _ in range(3):
    led_pin .value(1)  # Turn the LED on
    time.sleep(0.5)   # Wait for 0.5 seconds
    led_pin .value(0)  # Turn the LED off
    time.sleep(0.5)   # Wait for 0.5 seconds

led_pin .value(1)  # Turn the LED on
ugit.pull_all()
led_pin .value(0)
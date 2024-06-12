import sys
from machine import Pin, I2C
import time

# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from ssd1306 import SSD1306_I2C

def flash_led(pin, flashes):
    for _ in range(flashes):
        pin.value(1)  # Turn the LED on
        time.sleep(0.2)  # Wait for on_time seconds
        pin.value(0)  # Turn the LED off
        time.sleep(0.2)  # Wait for off_time seconds

# Define the onboard LED pin
led_pin = Pin(28, Pin.OUT)

i2c_dev = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
oled = SSD1306_I2C(128, 64, i2c_dev) # oled controller


oled.text('Hello World', 0, 0, 1)
oled.show()

# Flash the LED 3 times with 0.5 seconds on and 0.5 seconds off
flash_led(led_pin, 5)

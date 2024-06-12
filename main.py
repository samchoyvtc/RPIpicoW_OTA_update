import sys
from machine import Pin
import time

# Add the 'libs' directory to the module search path
sys.path.append('/Library')
import ssd1306

def flash_led(pin, flashes, on_time, off_time):
    """
    Flash the LED a specified number of times.

    :param pin: The Pin object for the LED
    :param flashes: Number of times to flash the LED
    :param on_time: Duration to keep the LED on (in seconds)
    :param off_time: Duration to keep the LED off (in seconds)
    """
    for _ in range(flashes):
        pin.value(1)  # Turn the LED on
        time.sleep(on_time)  # Wait for on_time seconds
        pin.value(0)  # Turn the LED off
        time.sleep(off_time)  # Wait for off_time seconds

# Define the onboard LED pin
led_pin = Pin(15, Pin.OUT)
# using default address 0x3C
i2c = I2C(sda=Pin(18), scl=Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Flash the LED 3 times with 0.5 seconds on and 0.5 seconds off
flash_led(led_pin, 3, 0.5, 0.5)
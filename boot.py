#boot.py
import ugit
from machine import Pin
import time

# Function to flash the onboard LED
def flash_led(pin, flashes, on_time, off_time):
    for _ in range(flashes):
        pin.value(1)  # Turn the LED on
        time.sleep(on_time)  # Wait for on_time seconds
        pin.value(0)  # Turn the LED off
        time.sleep(off_time)  # Wait for off_time seconds

# Initialize pin 15 as an input pin with a pull-up resistor
input_pin = Pin(15, Pin.IN, Pin.PULL_UP)

# Initialize the onboard LED pin
led_pin = Pin(28, Pin.OUT)

# Check if the input pin is low
if input_pin.value() == 0:
    # Flash the LED 3 times with 0.5 seconds on and 0.5 seconds off
    flash_led(led_pin, 5, 0.1, 0.1)
import ugit
from machine import Pin
import time

def flash_led(pin, flashes):
    for _ in range(flashes):
        pin.value(1)  # Turn the LED on
        time.sleep(0.2)  # Wait for on_time seconds
        pin.value(0)  # Turn the LED off
        time.sleep(0.2)  # Wait for off_time seconds

# Define the onboard LED pin
led_pin = Pin(28, Pin.OUT)
# Initialize pin 15 as an input pin with a pull-up resistor
input_pin = Pin(15, Pin.IN, Pin.PULL_UP)


# Check if the input pin is low
if input_pin.value() == 0:
    # Flash the LED 5 times
    flash_led(led_pin, 5)
    ugit.pull_all()
else:
    wlan = ugit.wificonnect()

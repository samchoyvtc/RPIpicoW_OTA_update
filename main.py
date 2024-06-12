from machine import Pin

# Define the onboard LED pin
led_pin = Pin(28, Pin.OUT)


while True:
    led_pin.value(1)  # Turn the LED on
    time.sleep(0.2)  # Wait for on_time seconds
    led_pin.value(0)  # Turn the LED off
    time.sleep(0.2)  # Wait for off_time seconds

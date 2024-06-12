import ugit
wlan = ugit.wificonnect()
led = Pin(28, Pin.OUT)

for _ in range(3):
    led.value(1)  # Turn the LED on
    time.sleep(0.5)   # Wait for 0.5 seconds
    led.value(0)  # Turn the LED off
    time.sleep(0.5)   # Wait for 0.5 seconds

led.value(1)  # Turn the LED on
ugit.pull_all()
led.value(0)

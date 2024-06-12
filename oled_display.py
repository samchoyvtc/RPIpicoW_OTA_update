import sys
from machine import Pin,I2C

# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from ssd1306 import SSD1306_I2C

def hello_world():
    i2c_dev = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
    oled = SSD1306_I2C(128, 64, i2c_dev) # oled controller

    oled.text('SSD1306 Ready', 15, 12, 1)
    oled.show()
    for _ in range():
        pin.value(1)  # Turn the LED on
        time.sleep(0.2)  # Wait for on_time seconds
        pin.value(0)  # Turn the LED off
        time.sleep(0.2)  # Wait for off_time seconds
    

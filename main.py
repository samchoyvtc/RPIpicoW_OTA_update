import sys
import time
from machine import Pin,I2C
import MQTT

# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from ssd1306 import SSD1306_I2C

def hello_world():
    i2c_dev = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
    oled = SSD1306_I2C(128, 64, i2c_dev) # oled controller

    count = 0
    for _ in range(255):
        str_count = str(count)
        count += 1
        oled.fill(0)  # Fill the screen with black (0 means off)
        oled.text('SSD1306', 15, 12, 1)
        oled.text(str_count, 15, 24, 1)
        oled.show()
        time.sleep(0.01)  # Wait for on_time seconds



    

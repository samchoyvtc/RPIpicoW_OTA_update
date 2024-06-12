import sys
import time
from machine import Pin,I2C

# Add the 'libs' directory to the module search path
sys.path.append('/Library')
from ssd1306 import SSD1306_I2C

def hello_world():
    i2c_dev = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
    oled = SSD1306_I2C(128, 64, i2c_dev) # oled controller

    oled.text('SSD1306 Ready', 15, 12, 1)
    oled.show()
    count = 0
    while True:
        count_string = str(count)
        oled.text(count_string, 15, 32, 1)
        time.sleep(0.5)
        count += 1
    
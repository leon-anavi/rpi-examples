from machine import Pin, I2C
import ssd1306

# using default address 0x3C
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c = I2C(0,sda=sda, scl=scl, freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello,', 0, 8, 1)
display.text('World!', 0, 16, 1)
display.show()
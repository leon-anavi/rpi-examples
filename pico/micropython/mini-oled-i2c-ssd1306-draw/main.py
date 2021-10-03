from machine import Pin, I2C
import ssd1306

# using default address 0x3C
sda=machine.Pin(4)
scl=machine.Pin(5)
i2c = I2C(0,sda=sda, scl=scl, freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.rect(0, 0, 128, 16, 1)
display.fill_rect(0, 0, 100, 16, 1)
for row in range(1, 4):
    for n in range(4):
        if row % 2:
            pos = 32*n
        else:
            pos = 16+32*n
        display.fill_rect(pos, row*16, 16, 16, 1)
display.show()
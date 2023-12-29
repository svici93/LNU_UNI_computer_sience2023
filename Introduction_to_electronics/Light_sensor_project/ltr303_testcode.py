
import time
import board
import busio
from adafruit_ltr329_ltr303 import LTR303
bgh7
i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA


time.sleep(0.1)  # sensor takes 100ms to 'boot' on power up
ltr303 = LTR303(i2c)

while True:
    print("Visible + IR:", ltr303.visible_plus_ir_light)
    print("Infrared    :", ltr303.ir_light)
    print()
    time.sleep(0.5)  # sleep for half a second

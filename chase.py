import board
from neopixel import NeoPixel
import time
import random
np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)


def chase(color):
    count = 0
    while True:
        for i in range(np.n):
            np.fill(color)	
        for i in range(np.n):
            if (i + count) % 4 == 0:
                np[i] = (0,0,0)
                
        time.sleep(0.1)
        np.show()
        count += 2
while True:
    chase((22,0,255))

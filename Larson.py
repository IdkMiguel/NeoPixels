import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)
i=0

red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
purple = (255, 127,0)
orange = (201, 75, 0)
blood = (117,18,0)
joker = (94,6, 143)
joke = (0,133,0)
ora = (136, 32, 0)
white = (255,255,255)

color_list = [red, green, blue, yellow, cyan]
def larson(bg,fg, num, delay = 0.5):
    direction = 0
    t = 1
    pixel = 0
    bounce_count = 0
    while bounce_count < num:
        np.fill(bg)
        np.show()           
        np[i] = fg
        np.show()
        t += direction
        if (t >= (np.n-1) or t <= 0):
            t *= -1
            bounce_count += 1
    time.sleep(0.05)
             

while True:
    rando = random.choice(color_list)
    larson(red, cyan, 5)


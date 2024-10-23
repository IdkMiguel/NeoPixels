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
ora = (136, 62, 0)

color_list = [blood, joke, joker, ora]
def fade_in(color):
    red_rat = color[0] / 50
    red_org = color[0]
    green_rat = color[1] / 50
    green_org = color[1]
    blue_rat = color[2] / 50
    blue_org = color[2]
    for i in range(1,51):
     red = red_org + i * red_rat
     green = green_org + i * green_rat
     blue = blue_org + i * blue_rat
     np.fill((red, green, blue))
     np.show()
     time.sleep(.05)
   
   

def fadeout(color):
    red_rat = color[0] / 50
    red_org = color[0]
    green_rat = color[1] / 50
    green_org = color[1]
    blue_rat = color[2] / 50
    blue_org = color[2]
    for i in range(1,51):
     red = red_org - i * red_rat
     green = green_org - i * green_rat
     blue = blue_org - i * blue_rat
     np.fill((red,green,blue))
     np.show()
     time.sleep(.05)
while True:
    rando = random.choice(color_list)
    fade_in(rando)
    fadeout(rando)


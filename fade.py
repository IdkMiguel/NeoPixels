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
orange = (255, 64, 0)

color_list = [red, green, blue, yellow, cyan, magenta, purple, orange]
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

fade_in(red)    
fadeout(red)
fade_in(green)    
fadeout(green)
fade_in(blue)    
fadeout(blue)

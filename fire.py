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


   
def fire(bck,flick,flick2,speed,t1):
    np.fill(bck)
    np.show()
    for i in range(t1):
        np[random.randint(0,np.n-2)] = flick
        np.show()
        time.sleep(speed)
        np[random.randint(0,np.n-2)] = flick2
        np.show()
        time.sleep(speed)
       
while True:
    fire((255,64,0),(255, 0, 0), (255, 55, 0),0.03,.4)

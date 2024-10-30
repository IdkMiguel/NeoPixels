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

color_list = [joke, joker, ora, blood]
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

def lightning(color):
    np.fill(color)
    np.show()
    time.sleep(random.randint(3,5))
    for i in range(random.randint(4,5)):
        np.fill((255,255,255))
        np.show()
        time.sleep(random.randint(3,5)/100)
        np.fill(color)
        np.show()
        time.sleep(random.randint(3,5)/100)

def sparkl(back = red, rg = ora, delay = 0.7, spark = 4):
    for i in range(spark):
        what = random.randint(0,29)
        who = random.randint(0,29)
        why = random.randint(0,29)
        np.fill(back)
        np[what] = rg
        np[who] = rg
        np[why] = rg
        np.show()
        time.sleep(delay)

def chase(color, hold = 0.1):
    count = 0
    for i in range(np.n):
        np.fill(color)
    for i in range(np.n):
        if (i + count) % 3 == 0:
            np[i] = ( 0,0,0)
                
        time.sleep(hold)
        np.show()
        count += 2




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
    rando = random.choice(color_list)
    chase(rando)
    fadeout(rando)
    fade_in(rando)
    lightning(rando)
    fire((rando),(rando), (rando),0.03,.4)
    sparkl()
    chase(rando)
    

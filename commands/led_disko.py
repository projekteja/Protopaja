import time
import board
import adafruit_dotstar as dotstar
import random

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
#Lights first two leds smoothly and then only a pair is on at once.


while True:
    
    a = random.randint(1,101)
    dots[0]=(0,0,0)
    dots[1]=(0,0,0)
    dots[2]=(0,0,0)
    
    if 1<a<33:
        dots[0]=(250,250,250)
    elif 33<a<66:
        dots[1]=(250,250,250)
    else:
        dots[2]=(250,250,250)
    
    time.sleep(0.05)
    
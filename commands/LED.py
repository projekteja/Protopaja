import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
#Lights first two leds smoothly and then only a pair is on at once.

def mato():

    dots[0]=(100,100,100)

    time.sleep(0.05)

    dots[1]=(100,100,100)

    time.sleep(0.05)

    while True:
        
        dots[2]=(100,100,100)
        dots[0]=(0,0,0)

        time.sleep(0.05)

        dots[0]=(100,100,100)
        dots[1]=(0,0,0)
        
        time.sleep(0.05)

        dots[1]=(100,100,100)
        dots[2]=(0,0,0)

        time.sleep(0.05)

def kummitus():

    a = 0
    b = 0
    
    while True:
        dots[0] = (a,a,a)
        dots[1] = (a,a,a)
        dots[2] = (a,a,a)


        if (b == 0):
            a += 3
        else:
            a -=3

        if (a > 250):
            b =1
            a = 250
            dots[0] = (a,a,a)
            dots[1] = (a,a,a)
            dots[2] = (a,a,a)
            time.sleep(1)

        if (a < 0):
            b = 0
            a = 0
            dots[0] = (a,a,a)
            dots[1] = (a,a,a)
            dots[2] = (a,a,a)
            time.sleep(1)
def off():

    dots[0]=(0,0,0)
    dots[1]=(0,0,0)
    dots[2]=(0,0,0)

def on():

    dots[0]=(0,0,0)
    dots[1]=(0,0,0)
    dots[2]=(0,0,0)


import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
#Lights first two leds smoothly and then only a pair is on at once.
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

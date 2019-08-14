import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
#Lights first two leds smoothly and then only a pair is on at once.

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
    

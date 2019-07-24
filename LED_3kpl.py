import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
a = 0
b = 0
while True:
    dots[0] = (a,a,a)
    dots[1] = (a,a,a)
    dots[2] = (a,a,a)

    if (b == 0):
        a += 5 
    else:
        a -=5 
    
    if (a > 250):
        b =1 
        a = 250
        time.sleep(1.5)
        
    if (a < 0):
        b = 0
        a = 0 
        time.sleep(1.5)
    print(a)
    
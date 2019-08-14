import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)
#Lights first two leds smoothly and then only a pair is on at once.
print("Leds on!!!")
dots[0]=(250,250,250)
dots[1]=(250,250,250)
dots[2]=(250,250,250)

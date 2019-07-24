import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)

dots[0]=(0,0,0)
dots[1]=(0,0,0)
dots[2]=(0,0,0)

print("LED OFF")

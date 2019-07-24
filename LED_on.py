import time
import board
import adafruit_dotstar as dotstar

dots=dotstar.DotStar(board.D6, board.D5, 3, brightness=1)

dots[0]=(100,100,100)
dots[1]=(100,100,100)
dots[2]=(100,100,100)

print("LED ON")



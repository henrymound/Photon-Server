import board
import neopixel
import sys
import random
import time

pixels = neopixel.NeoPixel(board.D18, 30)
for x in range(1, 30):
    colors = [(255, 146, 41),
              (255, 108, 41),
              (225, 146, 71),
              (225, 138, 25)]
    colorIndex = random.randint(0,len(colors) - 1)
    pixels[x] = colors[colorIndex]
    time.sleep(.05)

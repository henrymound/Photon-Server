import board
import neopixel
import sys
import random
import time

pixels = neopixel.NeoPixel(board.D18, 30)
while 1 == 1:
    colors = [(255, 146, 41),
              (255, 108, 41),
              (225, 146, 71),
              (225, 138, 25)]
    colorIndex = random.randint(0,len(colors) - 1)
    pixelIndex = random.randint(0, 30)
    pixels[pixelIndex] = colors[colorIndex]
    time.sleep(.05)

import board
import neopixel
import sys

pixels = neopixel.NeoPixel(board.D18, 30)
for x in range(1, 30):
    pixels[x] = (r, g, b)

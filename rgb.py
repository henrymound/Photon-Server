import board
import neopixel
import sys

if len(sys.argv) == 4:
    # print("Got 3 RGB Values!")
    r = sys.argv[1]
    g = sys.argv[2]
    b = sys.argv[3]
    # print("R: " + r)
    # print("G: " + g)
    # print("B: " + b)
    pixels = neopixel.NeoPixel(board.D18, 30)
    pixels.fill((r, g, b))

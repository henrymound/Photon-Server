import board
import neopixel
import sys

if len(sys.argv) == 4:
    # print("Got 3 RGB Values!")
    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])
    # print("R: " + r)
    # print("G: " + g)
    # print("B: " + b)
    pixels = neopixel.NeoPixel(board.D18, 144, pixel_order=neopixel.RGBW)
    pixels.fill((r, g, b, 0))

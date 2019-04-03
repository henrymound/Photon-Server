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
    pixels.fill((g, r, b, 0))
else if len(sys.argv) == 5:
    # print("Got 4 RGBW Values!")
    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])
    w = int(sys.argv[4])
    # print("R: " + r)
    # print("G: " + g)
    # print("B: " + b)
    # print("W: " + w)
    pixels = neopixel.NeoPixel(board.D18, 144, pixel_order=neopixel.RGBW)
    pixels.fill((g, r, b, w))

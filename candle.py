import board
import neopixel
import sys
import random
import time

TOLERANCE = 30 # The difference between range values
NUMCOLORS = 10 # The number of different random colors generated for the effect
NUMLIGHTS = 30 # The number of lights on the Photon

if len(sys.argv) == 4:
    # print("Got 3 RGB Values!")
    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])

    # Get upper and lower values
    rLower = r - TOLERANCE
    rUpper = r + TOLERANCE

    gLower = g - TOLERANCE
    gUpper = g + TOLERANCE

    bLower = b - TOLERANCE
    bUpper = b + TOLERANCE

    # Make sure all the values are within the range (0, 255)
    if(rLower < 0):
    	rLower = 0
    if(rUpper > 255):
    	rUpper = 255
    if(gLower < 0):
    	gLower = 0
    if(gUpper > 255):
    	gUpper = 255
    if(bLower < 0):
    	bLower = 0
    if(bUpper > 255):
    	bUpper = 255

	pixels = neopixel.NeoPixel(board.D18, 30)
	while 1 == 1:
		# Generate an array of random colors based on provided color
		colors = [
				(random.randint(rLower,rUpper),
				 random.randint(gLower,gUpper),
				 random.randint(bLower,bUpper))
			 for _ in range(NUMCOLORS)]
	    colorIndex = random.randint(0,len(colors) - 1)
	    pixelIndex = random.randint(0, NUMLIGHTS - 1)
	    pixels[pixelIndex] = colors[colorIndex]
	    time.sleep(.005)

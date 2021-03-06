import time
import board
import neopixel
import time

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def stripCode():
	# Set counter and loop vars
	x = 1
	loop = 0
	print("accel")
	while loop == 0:
		# Keep checking for stop signals
		h = open("status.txt", "r")
		status = h.read()
		h.close()
		if status == "STOP":
			loop = 1
		# Run actual strip code
		rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
		x = x + 1
 
# Order all current running programs to STOP
f = open("status.txt", "w")
f.write("STOP")
f.close()

# Wait for them to do so
time.sleep(1)

# Set status to represent script is running
f = open("status.txt", "w")
f.write("RUN")
f.close()
	
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 144

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGBW

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)

# Run body code after check has been performed
stripCode()	


    


import time

def accelCode():
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
			print("Accel Status is 'STOP' after " + str(x) + "iterations.")
			loop = 1
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

# Run body code after check has been performed
accelCode()	
	



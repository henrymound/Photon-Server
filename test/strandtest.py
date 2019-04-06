x = 1
loop = 0
# This loop waits for the green light for the code to start
while loop == 0:
	h = open("status.txt", "r")
	status = h.read()
	h.close()
	if status == "RUN":
		j = open("status.txt", "w")
		j.write("STOP")
		j.close()
	if status == "STOPPED":
		print("Other Code Has Stopped. Accel Will Start.")
		l = open("status.txt", "w")
		l.write("RUN")
		l.close()
		accelCode()
	x = x + 1


# This code for the program always listens for termination
def accelCode():
	j = open("status.txt", "w")
	j.write("RUN")
	j.close()
	x = 0
	while loop == 0:
		# Accel code
		print("Strand test")
		if status == "STOP":
			print("Strand Test Read Status is 'STOP' after " + str(x) + "iterations.")
			l = open("status.txt", "w")
			l.write("STOPPED")
			l.close()
			loop = 1
	x = x + 1	
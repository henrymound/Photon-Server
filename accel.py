#!/usr/bin/python
import smbus
import math
import time
import board
import neopixel
import sys

# Order all current running programs to STOP
f = open("status.txt", "w")
f.write("STOP")
f.close()

# Wait for them to do so
time.sleep(.5)

# Set status to represent script is running
f = open("status.txt", "w")
f.write("RUN")
f.close()

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)
#pixels = neopixel.NeoPixel(board.D18, 144, pixel_order=neopixel.RGBW)
pixels = neopixel.NeoPixel(board.D18, 144, pixel_order=neopixel.RGBW)

loop = 0
while loop == 0:
    # Check for stop signal
    h = open("status.txt", "r")
    status = h.read()
    h.close()
    
    if status == "STOP":
        #print("Accel Status is 'STOP' after " + str(x) + "iterations.")
        loop = 1
        break

    time.sleep(0.03)

    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    #print ("gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131))
    #print ("gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131))
    #print ("gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131))

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    #print ("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
    #print ("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
    #print ("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)

    #print ("x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    #print ("y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    
    accel_r = accel_xout_scaled
    accel_g = accel_yout_scaled
    accel_b = accel_zout_scaled
    
    accel_r = int(accel_r*255)
    accel_g = int(accel_g*255)
    accel_b = int(accel_b*255)
    
    if accel_r < 0: accel_r = accel_r * -1
    if accel_b < 0: accel_b = accel_b * -1
    if accel_g < 0: accel_g = accel_g * -1
    
    if accel_r > 255: accel_r = 255
    if accel_b > 255: accel_b = 255
    if accel_g > 255: accel_g = 255

    pixels.fill((int(accel_r), int(accel_g), int(accel_b), 0))
    print("Filling with R: "+str(int(accel_r))+" G: "+str(int(accel_g))+" B: "+str(int(accel_b)))
    

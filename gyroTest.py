###
 # Author			: E J Jonkers
 # date created		: 30-03-15
 #
###

from __future__ import division
import l3gd20H
from time import sleep
from copy import copy


G = l3gd20H.gyro(8) #mine is at I2C bus 8
G.enableDefault()

barCounter = 0
print "Now start jerking your sensor!"
print "hit <cntrl>-c to quit"
spaceString = list("                                                                ")
barString   = list("----------------------------------------------------------------")
while True:

	barCounter += 1
	if barCounter == 10:
		barCounter = 0
		outString = copy(barString)
	else:
		outString = copy(spaceString)

	(x, y, z) = G.read()
	print (x, y, z)
	i = 11 + int(x/3277) # +/-32768 = max scale
	outString[i] = ':'
	i = 32 + int(y/3277)
	outString[i] = ':'
	i = 53 + int(z/3277)
	outString[i] = ':'
#	print "".join(outString)
	sleep(0.010)

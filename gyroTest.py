###
 # Author			: E J Jonkers
 # date created		: 30-03-15
 #
###

from __future__ import division,print_function
import l3gd20H
from time import sleep


G = l3gd20H.gyro(8) #mine is at I2C bus 8
G.enableDefault()

print "hit <cntrl>-c to quit"
while True:
	spaceString = "                                                                "
	barString   = "----------------------------------------------------------------"

	barCounter++
	if barCounter == 10:
		barCounter = 0
		outString = barString
	else:
		outString = spaceString

		g = G.read()
		i = 11 + int(g.x/3277) # +/-32768 = max scale
		outString[i] = ':'
		i = 32 + int(g.y/3277)
		outString[i] = ':'
		i = 53 + int(g.y/3277)
		outString[i] = ':'
		print (outString, end='\r')
		sleep(20)

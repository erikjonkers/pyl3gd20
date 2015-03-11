###
 # Author			: E J Jonkers
 # date created		: 11-03-15
 #
 # http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc
###

import smbus

WHO_AM_I = 0x0F
CTRL1 = 0x20
CTRL2 = 0x21
CTRL3 = 0x22
CTRL4 = 0x23
CTRL5 = 0x24
REFERENCE = 0x25
OUT_TEMP = 0x26
STATUS = 0x27
OUT_X_L = 0x28
OUT_X_H = 0x29
OUT_Y_L = 0x2A
OUT_Y_H = 0x2B
OUT_Z_L = 0x2C
OUT_Z_H = 0x2D
FIFO_CTRL = 0x2E
FIFO_SRC = 0x2F
IG_CFG = 0x30
IG_SRC = 0x31
IG_THS_XH = 0x32
IG_THS_XL = 0x33
IG_THS_YH = 0x34
IG_THS_YL = 0x35
IG_THS_ZH = 0x36
IG_THS_ZL = 0x37
IG_DURATION = 0x38
LOW_ODR = 0x39

class gyro:
	def __init__(self, i2cbus=0, address=0x6b ):
		self.bus = smbus.SMBus(i2cbus)
		self.address = address
	def enableDefault(self):
		# copied from pololu's arduino library: https://github.com/pololu/l3g-arduino/blob/master/L3G/L3G.cpp
		#Enables the L3G's gyro. Also:
		#- Sets gyro full scale (gain) to default power-on value of +/- 250 dps
		#(specified as +/- 245 dps for L3GD20H).
		#- Selects 200 Hz ODR (output data rate). (Exact rate is specified as 189.4 Hz
		#for L3GD20H and 190 Hz for L3GD20.)
		#Note that this function will also reset other settings controlled by
		#the registers it writes to.

		# Low_ODR = 0 (low speed ODR disabled)
		self.writeRegister(LOW_ODR, 0x00)

		# FS = 00 (+/- 250 dps full scale)
		self.writeRegister(CTRL4, 0x00)

		# DR = 01 (200 Hz ODR); BW = 10 (50 Hz bandwidth); PD = 1 (normal mode); Zen = Yen = Xen = 1 (all axes enabled)
		self.writeRegister(CTRL1, 0x6F)

	def readRegister(self, registerAddress):
		return self.bus.read_byte_data(self.address, registerAddress)
	def writeRegister(self, registerAddress, dataByte):
		return self.bus.write_byte_data(self.address, registerAddress, dataByte)
	def read(self):
		xl = self.readRegister(OUT_X_L);
		xh = self.readRegister(OUT_X_H);
		yl = self.readRegister(OUT_Y_L);
		yh = self.readRegister(OUT_Y_H);
		zl = self.readRegister(OUT_Z_L);
		zh = self.readRegister(OUT_Z_H);

		x = xh << 8 | xl
		y = yh << 8 | yl
		z = zh << 8 | zl
		return (x, y, z)


#!/usr/bin/python

import binascii

with open('ch7.bin','rb') as f:
		hexdata = binascii.hexlify(f.read())
		hexlist = map(''.join, zip(hexdata[::2], hexdata[1::2]))

for i in range(256):
	message=[chr((int(c,16)+i)%256) for c in hexlist]
	result=''.join(message)
	print('%i : %s' % (i,result))


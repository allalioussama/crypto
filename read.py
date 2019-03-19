#!/usr/bin/python

import binascii


with open('binaryfile.bin','rb') as f:
		hexdata = binascii.hexlify(f.read())
		hexlist = map(''.join, zip(hexdata[::2], hexdata[1::2]))

for i in range(256):
	message=[chr((int(c,16)+i)%256) for c in hexlist]
	result=''.join(message)
	print('%i : %s' % (i,result))

#ord() function in python return an integer representing the Unicode code  of the character .
#it 'is the reverse of chr() :example ord('a')=97:chr(97)=a

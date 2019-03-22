#! /use/bin/python


def decrypt(ciphertext,key):
		result=""

		for i in range(len(ciphertext)):
				char=ciphertext[i]

				if(char.isupper()):
						result+=chr((ord(char)+key-ord('A'))%26+ord('A'))
				else:
						result+=chr((ord(char)+key-ord('a'))%26+ord('a'))

		return result

if __name__	==	'__main__':
		cipher="""
tm bcsv qolfp
f dmvd xuhm exl tgak
hlrkiv sydg hxm
qiswzzwf qrf oqdueqe
dpae resd wndo
liva bu vgtokx sjzk
hmb rqch fqwbg
fmmft seront sntsdr pmsecq
"""
		i	=	1
		debut	=	""
		fin	=	""
		output=	""
		for ligne in cipher.splitlines():
				line=""
				for mot in ligne.split():
						output	+=	decrypt(mot,i)
						line	+=	decrypt(mot,i)
						i       += 1
						output	+=" "
				output	+=	"\n"
				if  line != "":
						debut	+=	line[0]
						fin	+=	line[-1]

print "cipherText :"+cipher
print "original Text"+output
print "%s%s" % (debut,fin)


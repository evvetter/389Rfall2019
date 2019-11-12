#!/usr/bin/env python2



import sys

import struct

from datetime import date




# You can use this method to exit on failure conditions.

def bork(msg):

    sys.exit(msg)





# Some constants. You shouldn't need to change these.

MAGIC = 0x8BADF00D

VERSION = 1

index = 8

if len(sys.argv) < 2:

    sys.exit("Usage: python stub.py input_file.fpff")



# Normally we'd parse a stream to save memory, but the FPFF files in this

# assignment are relatively small.

with open(sys.argv[1], 'rb') as fpff:

    data = fpff.read()



# Hint: struct.unpack will be VERY useful.

# Hint: you might find it easier to use an index/offset variable than

# hardcoding ranges like 0:8

magic, version = struct.unpack("<LL", data[0:8])


stamp, author = struct.unpack("<L8s", data[index:index+12])

index+=12


snum, garb = struct.unpack("<L0s", data[index:index+4])
index+=4



if magic != MAGIC:

    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))



if version != VERSION:

    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))



print("------- HEADER -------")

print("MAGIC: %s" % hex(magic))
print("Version: %d" % int(version))

print(date.fromtimestamp(int(stamp)))

print("Author: %s" % author.decode("utf-8"))

print("Section count: %d" % int(snum))

# We've parsed the magic and version out for you, but you're responsible for

# the rest of the header and the actual FPFF body. Good luck!



print("-------  BODY  -------")
snum = int(snum)
i=1
while i <= snum:
	print("Section %d" % i)
	i+=1
	stype, slen = struct.unpack("<LL", data[index:index+8])
	index+=8
	if(int(slen)>0):
		print(stype)
		if stype == 1:
			sval = data[index:index+slen]
			index+=slen
			print(sval.decode("ascii"))
		elif stype == 0x2:
			sval = data[index:index+slen]
			index+=slen
			print(sval.decode("utf-8"))	
		elif stype == 0x3:
			i = 0
			while i < slen/4:
				print(data[index:index+4])
				index+=4
				i+=1
		elif stype == 0x4:
			i = 0
			while i < slen/8:
				print(data[index:index+8])
				index+=8
				i+=1
		elif stype == 0x5:
			i = 0
			while i < slen/8:
				print(float(data[index:index+4]))
				index+=8
				i+=1
		elif stype == 0x6:
			a, b = struct.unpack("<dd", data[index:index+16])
			index+=16
			print(a, b)	
		elif stype == 0x7:
			a = sval[index:index+4]
			print(a)
		elif stype == 0x8:
			sval = data[index:index+slen]
			index+=slen			
			f = open("img.png", "wra+")
			f.write(chr(0x89))
			f.write(chr(0x50))
			f.write(chr(0x4E))
			f.write(chr(0x47))
			f.write(chr(0x0D))
			f.write(chr(0x0A))
			f.write(chr(0x1A))
			f.write(chr(0x0A))
			f.write(sval)
		elif stype == 0x9:
			sval = data[index:index+slen]
			index+=slen			
			f = open("img.gif", "wra+")
			f.write(chr(0x47))
			f.write(chr(0x49))
			f.write(chr(0x46))
			f.write(chr(0x38))
			f.write(chr(0x37))
			f.write(chr(0x61))
			f.write(sval)
		elif stype == 0xA:
			sval = data[index:index+slen]
			index+=slen			
			f = open("img2.gif", "wra+")
			f.write(chr(0x47))
			f.write(chr(0x49))
			f.write(chr(0x46))
			f.write(chr(0x38))
			f.write(chr(0x37))
			f.write(chr(0x61))
			f.write(sval)
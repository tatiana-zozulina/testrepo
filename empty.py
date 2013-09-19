#!/usr/local/bin/python

import sys

def subtr(a,b):
	c = a-b
	print "Subtraction result:", c
	return c

def main():
	print "Command-line arguments:"
	print sys.argv
	x = raw_input("Please, enter first number: ")
	y = raw_input("Please, enter second number: ")
	try:
		x = int(x)
		y = int(y)
	except ValueError:
		print "Unexpected value."
		return
	z = subtr(x,y)

if __name__ == "__main__":
	main()

#end of homework
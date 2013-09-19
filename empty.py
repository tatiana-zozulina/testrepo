#!/usr/local/bin/python

import sys


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
	z = x-y
	print "Subtraction result:", z

if __name__ == "__main__":
	main()
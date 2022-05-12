#!/usr/bin/python3

# Read form the file
flag = open('enc').read()

for i in range(len(flag)):
	# Return Unicode code from a character then convert it to Hex
	a = hex(ord(flag[i]))

	# Convert Hex to ASCII and print it
	b = bytes.fromhex(a[2:]).decode()
	print(b, end='')

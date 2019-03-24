#!/usr/bin/python3

# File:		increment_digits.py
# Author:	Brett Henderson
# Contact:	brett.henderson@bremily.net
# Created:	2019-03-24
#
# Purpose:	Take a number from the user and print a new number by incrementing each digit by 1.

# Loop over each character of the input string and increment by 1
def increment_digits(number):
	ans = ''
	for digit in number:
		ans += str(int(digit) + 1)
	return ans

number = (input('Enter a number: '))
new_number = increment_digits(number)

print()
print('Old number: ' + number)
print('New number: ' + new_number)


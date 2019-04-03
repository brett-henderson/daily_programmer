#!/usr/bin/python3

# File:		increment_digits_bonus.py
# Author:	Brett Henderson
# Contact:	brett.henderson@bremily.net
# Created:	2019-04-03
#
# Purpose:	Take a number from the user and print a new number by incrementing each digit by 1.

import math

def increment_digits(number):
    number_new = 0
    digits = int(math.log10(number) + 1)
    position = 1

    while digits:
        number_tmp = (number % 10) + 1      # Grab the right most digit and increment
        number //= 10                       # Remove it from the original number
        number_new += number_tmp * position # Place it from right to left

        # Position the digit to the left of the current number
        if number_tmp == 10:
            position *= 100     # 2 digits to the left
        else:
            position *= 10      # 1 digit to the left
        digits -= 1

    return number_new

number = int(input('Enter a number: '))
number_new = increment_digits(number)

print("Old: " + str(number))
print("New: " + str(number_new))

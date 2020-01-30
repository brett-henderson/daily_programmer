#!/usr/bin/python3

import math


def increment_digits(number):
    number_new = 0
    digits = int(math.log10(number) + 1)
    position = 1

    while digits:
        number_tmp = (number % 10) + 1       # Increment right most digit
        number //= 10                        # Remove it from number
        number_new += number_tmp * position  # Place it at current position

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

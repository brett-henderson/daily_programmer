#!/usr/bin/python3

import math

def additive_persistence(number):
    # Calculate the sum of the number by looping through its digits
    digits = int(math.log10(number) + 1) # number length
    add = 0 # the sum value

    while digits:
        add += number % 10  # add the right most digit
        number //= 10       # remove the right most digit
        digits -= 1

    return add

number = int(input("Enter a number: "))
answer = number # Keep number unchanged for final output
count = 0 # The additive persistence value

# The number will change to the sum of its digits until that
# sum is only 1 digit long
while answer > 9:
    answer = additive_persistence(answer)
    count += 1

print(str(number) + ' -> ' + str(count))

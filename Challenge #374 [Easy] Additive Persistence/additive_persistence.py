#!/usr/bin/python3

def additive_persistence(number):
    # Loop backwards through each digit of the number and
    # return the sum of its digits
    add = 0
    for i in range(len(number)-1,-1,-1):
        add += int(number[i])
    return str(add)

number = input("Enter a number: ")
answer = number # Keep number unchanged for final output
count = 0 # The additive persistence value

# The number will change to the sum of its digits until that
# sum is only 1 digit long
while len(answer) > 1:
    answer = additive_persistence(answer)
    count += 1

print(number + ' -> ' + str(count))

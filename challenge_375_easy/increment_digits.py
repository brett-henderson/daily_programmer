#!/usr/bin/python3

# Loop over each character of the input string and increment by 1
def increment_digits(number):
	ans = ''
	for digit in number:
		ans += str(int(digit) + 1)
	return ans

number = (input('Enter a number: '))
number_new = increment_digits(number)

print()
print('Old number: ' + number)
print('New number: ' + number_new)


# Numbers and numerals
import random
import re  # Palindrome number
import math  # Square root

# Generate random values
print("Calculating numbers...")
addition_goal = (
	random.randint(1, 20) + 4 + 18 + 2 + 27
)  # 4+18 for binary and hex. 2 for prime. 27 for history date
binary_goal = bin(random.randint(0, 15))[2:]
hex_goal = hex(random.randint(0, 255))[2:]
numeral_goal = random.randint(3, 49)


# Numbers must add to random number + other required numbers
def addition(i, password):
	# Add up all numbers in to total
	t = 0
	for c in password:
		if c in "0123456789":
			# Add to total
			t += int(c)
	# Check total
	if t == addition_goal:
		return True  # Passed
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": The digits in the password must add to "
		+ str(addition_goal)
		+ "."
	)
	return False


# Prime digit
def prime(i, password):
	# Check if each character is prime
	for c in password:
		if c in "2357":
			return True
	# Did not pass
	print("Rule " + str(i) + ": Password must a single digit prime number.")
	return False


# 4 bit Binary for a random number between 0 and 15
def binary(i, password):
	# Check if binary goal in password
	if binary_goal in password:
		return True
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": Password must contain the binary for "
		+ str(int(binary_goal, 2))
		+ "."
	)
	return False


# 2 digit hexadecimal for a random number
def hexadecimal(i, password):
	# Check if hexadecimal goal in password
	if hex_goal in password:
		return True
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": Password must contain the hexadecimal for "
		+ str(int(hex_goal, 16))
		+ "."
	)
	return False


# Contain a palindrome number
def palindrome(i, password):
	# Get numeric substrings
	x = re.findall(r'\d+', password)
	for y in x:
		if y >= 4:
			if y == y[::-1]:
				return True
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": Password must include a 4 character or more palindrome number."
	)
	return False

# Basic rules present in most NORMAL password checkers


# First rule
def initial(i, password):
	# Check if blank
	if password == "":
		print("Please enter a password.")
		return False
	return True


# Include a number
def number(i, password):
	# Check if a number is in the password
	for n in range(10):
		if str(n) in password:
			return True  # Passed
	# Did not pass
	print("Rule " + str(i) + ": Password must include a number.")
	return False


# Include a symbol
def symbol(i, password):
	# Check if a symbol is in the password
	for c in "!£$%&*@#~.,-=_+":
		if c in password:
			return True  # Passed
	# Did not pass
	print("Rule " + str(i) + ": Password must include a symbol.")
	return False


# Greater than 5 characters
def length(i, password):
	# Check character count
	if len(password) >= 5:
		return True  # Passed
	# Did not pass
	print("Rule " + str(i) + ": Password must include 5 or more characters.")
	return False


# Includes a capital letter
def capital(i, password):
	# Check each character that isnt a number
	for c in password:
		if c not in "0123456789":
			if c == c.upper():
				return True
	# Did not pass
	print("Rule " + str(i) + ": Password must include a capital letter.")
	return False

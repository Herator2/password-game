# English based checks

# Contains a palindrome
def palindrome(i, password):
	# Get password length
	n = len(password)
	# Check all substrings of the password
	for x in range(n):
		# Substrings of length 2 or more
		for j in range(x + 5, n + 1):
			if password[x:j] == password[x:j][::-1]:
				return True
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": Password must include a five character or more palindrome."
	)
	return False

# Consecutive lower or upper case
def consecutive(i, password):
	# Set value for last character state
	last_upper = False
	# Loop through password
	for x in range(len(password)-1):
		# Check upper
		if password[i].isupper() and password[i + 1].isupper():
			print("Rule " + str(i) + ": Password must not contain two consecutive upper case characters.")
			return False
		# Check lower
		if password[i].islower() and password[i + 1].islower():
			print("Rule " + str(i) + ": Password must not contain two consecutive lower case characters.")
			return False
	# Passed
	return True

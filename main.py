import readline  # Readline module required to use input prefill
import os  # OS used to clear screen
from sys import platform  # Test operating system

# Only tested on linux: https://stackoverflow.com/questions/2533120/show-default-value-for-editing-on-python-input-possible
def rlinput(prompt, prefill=""):
	# Check for linux
	if platform == "linux" or platform == "linux2":
		readline.set_startup_hook(lambda: readline.insert_text(prefill))
		try:
			return input(prompt)  # or raw_input in Python 2
		finally:
			readline.set_startup_hook()
	# Basic input without prefill
	return input(prompt)

# Clear screen using a command
def clear():
	# Windows
	if platform == "win32":
		os.system("cls")
	# Linux / Mac
	else:
		os.system("clear")

# Import rule modules
import basic
import english
import numerals
import colors
import history
import geography
import stupid

# Main rules
rules = [
	basic.initial,
	basic.length,
	basic.capital,
	basic.number,
	basic.symbol,
	numerals.addition,
	numerals.prime,
	colors.primary,
	numerals.binary,
	english.palindrome,
	colors.secondary,
	numerals.hexadecimal,
	colors.hextotext,
	colors.multiplesecondary,
	history.date,
	stupid.wordle,
	geography.capital,
	stupid.phonetic,
	geography.continent,
]

# Setup other persistent variables
password = ""

# Main gameplay loop
while True:
	# Clear screen
	clear()

	# Check each rule
	rule_failed = False
	for rule in rules:
		# Get current index
		i = rules.index(rule)
		# Run rule method and get result
		if rule.__call__(i, password):
			# Rule passed
			continue  # Try next rule
		# Rule failed
		rule_failed = True
		break

	# Determine if all rules had passed
	if not rule_failed:
		print("Password is viable.")
		break

	# Print spacer or hint
	if password == "":
		print("  HINT -> Hit enter to check typed password")
	else:
		print()

	# Ask user for password to check with a prefill of the last password
	password = rlinput(" >>> ", password)

# For the lols
x = 0
while True:
	# Ask for password
	print("For security reasons, please reenter your password")
	x = rlinput(" >>> ", x)

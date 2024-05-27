# Geography based rules
import random

# Random persistent values
capital_city = random.choice(
	[
		{"country": "england", "capital": "london"},
		{"country": "japan", "capital": "tokyo"},
		{"country": "russia", "capital": "moscow"},
		{"country": "netherlands", "capital": "amsterdam"},
		{"country": "italy", "capital": "rome"},
		{"country": "south korea", "capital": "seoul"},
		{"country": "spain", "capital": "madrid"},
		{"country": "france", "capital": "paris"},
		{"country": "germany", "capital": "berlin"},
		{"country": "thailand", "capital": "bangkok"},
		{"country": "china", "capital": "beijing"},
	]
)


# Password needs to contain a capital city from a random country
def capital(i, password):
	# Check for capital
	if capital_city["capital"] in password.lower():
		return True
	# Did not pass
	print(
		"Rule "
		+ str(i)
		+ ": Password must contain the capital city of "
		+ str(capital_city["country"].title())
		+ "."
	)
	return False


# Include a continent
def continent(i, password):
	# Check if password includes one of the continents (With a couple extras to avoid confusion)
	for x in [
		"europe",
		"america",
		"africa",
		"asia",
		"antarctica",
		"oceania",
		"australia",
		"australasia",
	]:
		if x in password.lower():
			return True
	# Did not pass
	print("Rule " + str(i) + ": Password must contain a continent.")
	return False

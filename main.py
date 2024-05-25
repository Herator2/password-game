import readline  # Readline module required to use input prefill
import os  # OS used to clear screen


# Only tested on linux: https://stackoverflow.com/questions/2533120/show-default-value-for-editing-on-python-input-possible
def rlinput(prompt, prefill=""):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)  # or raw_input in Python 2
    finally:
        readline.set_startup_hook()


# Import rule modules
import basic
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
    numerals.prime,
    numerals.numeral,
    colors.primary,
    numerals.addition,
    numerals.binary,
    colors.secondary,
    numerals.hexadecimal,
    colors.hextotext,
    colors.multiplesecondary,
    history.date,
    geography.capital,
    stupid.phonetic,
]

# Setup other persistent variables
password = ""

# Main gameplay loop
while True:
    # Clear screen
    os.system("clear")

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
        print("Password is viable.\n - In other words, you won!")
        break

    # Print spacer or hint
    if password == "":
        print("  HINT -> Hit enter to check typed password")
    else:
        print()

    # Ask user for password to check with a prefill of the last password
    password = rlinput(" >>> ", password)

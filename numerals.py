# Numbers and numerals
import random

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


# Contain a random roman numeral
def numeral(i, password):
    # Check each character for a start to roman numerals
    for c in password:
        if c in "IVXLCDM":
            # Setup first element of the numeral
            numeral = c
            # Setup current value
            x = password.index(c)
            # Test next term
            while True:
                # At last character in password
                if x == len(password) - 1:
                    print("END OF SEQUENCE")
                    break
                # Increment pointer / Current value
                x += 1
                # Test if pointer is on a roman numeral
                if password[x] in "IVXLCDM":
                    # Add to main numeral and go to top of loop
                    numeral = numeral + password[x]
                    print("ADD:", password[x])
                    continue
                # Not a numeral -> Break out of loop
                print("NOT NUMERAL:", password[x])
                break
            # Translate into numbers
            value_map = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }
            value = 0
            last_digit_value = 0
            print("TRANSLATING:", numeral)
            # Translation algorithm
            for roman_digit in numeral[::-1]:
                digit_value = value_map[roman_digit]
                if digit_value >= last_digit_value:
                    value += digit_value
                    last_digit_value = digit_value
                else:
                    value -= digit_value
            # Test if value matches
            if value == numeral_goal:
                return True
    # Did not pass
    print(
        "Rule "
        + str(i)
        + ": Password must contain the roman numerals for "
        + str(numeral_goal)
        + "."
    )
    return False

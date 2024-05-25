# Random collection of stupid rules
import random

# Generate random persistent values
phonetic_morse = [
    ".- .-.. .--. .... .-",
    "-... . - .-",
    "--. .- -- -- .-",
    "-.-. .... .- .-. .-.. .. .",
    "-.. . .-.. - .-",
    ". -.-. .... ---",
    "..-. --- -..- - .-. --- -",
    "--. --- .-.. ..-.",
    ".... --- - . .-..",
    ".. -. -.. .. .-",
    ".--- ..- .-.. .. . - -",
    "-.- .. .-.. ---",
    ".-.. .. -- .-",
    "-- .. -.- .",
    "-. --- ...- . -- -... . .-.",
    "--- ... -.-. .- .-.",
    ".--. .- .--. .-",
    "--.- ..- . -... . -.-.",
    ".-. --- -- . ---",
    "... .. . .-. .-. .-",
    "- .- -. --. ---",
    "..- -. .. ..-. --- .-. --",
    "...- .. -.-. - --- .-.",
    ".-- .... .. ... -.- . -.--",
    "-..- .-. .- -.--",
    "-.-- .- -. -.- . .",
    "--.. ..- .-.. ..-"
]


# Check for a letter from the phonetic alphabet in morse code
def phonetic(i, password):
    # Check each character
    for s in phonetic_morse:
        if s in password:
            return True
    # Did not pass
    print("Rule "+str(i)+": Password must contain a letter from the phonetic alphabet in morse code.")
    return False





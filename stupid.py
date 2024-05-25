# Random collection of stupid rules
import random
import requests  # Used to get wordle data from nytimes
from datetime import datetime  # Used to get the date for the wordle answer

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
    "--.. ..- .-.. ..-",
]

# Get wordle answer from https://www.nytimes.com/svc/wordle/v2/YYYY-MM-DD.json
print("Fetching wordle data...")
current_date = datetime.now().date()
wordle_ans = requests.get(
    "https://www.nytimes.com/svc/wordle/v2/"
    + current_date.strftime("%Y-%m-%d")
    + ".json"
).json()["solution"]


# Check for a letter from the phonetic alphabet in morse code
def phonetic(i, password):
    # Check each character
    for s in phonetic_morse:
        if s in password:
            return True
    # Did not pass
    print(
        "Rule "
        + str(i)
        + ": Password must contain a letter from the phonetic alphabet in morse code."
    )
    return False


# Check wordle answer
def wordle(i, password):
    # Test already cached answer against password
    if wordle_ans in password.lower():
        return True
    # Did not pass
    print("Rule " + str(i) + ": Password must contain todays wordle answer.")
    return False

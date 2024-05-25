# A couple different color based ones
import random

color_choice = random.choice(
    ["FF0000", "00FF00", "0000FF", "FFFF00", "00FFFF", "FF00FF"]
)  # Red Green Blue Yellow Cyan Magenta


# Must contain only two primary colors
def primary(i, password):
    # Check if password has primary color
    x = 0
    for color in ["blue", "red", "green"]:
        if color in password.lower():
            x += 1
    # Pass check
    if x == 2:
        return True
    # Did not pass
    if x == 1:
        print(
            "Rule "
            + str(i)
            + ": Password must include one more primary color (Science/Computing based primary colors)."
        )
    elif x > 2:
        print(
            "Rule "
            + str(i)
            + ": Password must include only two primary colors (Science/Computing based primary colors)."
        )
    else:
        print(
            "Rule "
            + str(i)
            + ": Password must include two primary colors (Science/Computing based primary colors)."
        )
    return False


# Must contain the mix of the two primary colors
def secondary(i, password):
    # Get the first 2 primary colours
    colors = []
    for color in ["blue", "red", "green"]:
        if color in password.lower():
            if color not in colors and len(colors) < 2:
                colors.append(color)
    # Decide what the mixture is
    x = []
    if "blue" in colors and "red" in colors:
        x = ["magenta", "purple", "pink", "lilac", "violet"]
    elif "red" in colors and "green" in colors:
        x = ["yellow"]
    elif "green" in colors and "blue" in colors:
        x = ["cyan", "turquoise"]
    # Test if mixture is in password
    for y in x:
        if y in password.lower():
            return True
    # Did not pass
    print(
        "Rule "
        + str(i)
        + ": Password must include the mixture of your two primary colors."
    )
    return False


# Must only contain a single secondary color
def multiplesecondary(i, password):
    # Count up each color
    t = 0
    for c in [
        "magenta",
        "purple",
        "pink",
        "lilac",
        "violet",
        "yellow",
        "cyan",
        "turquoise",
    ]:
        if c in password.lower():
            t += 1
    # Test if there is less than or equal to 1 in total
    if t <= 1:
        return True
    # Did not pass
    print("Rule " + str(i) + ": Password must only contain a single secondary color.")
    return False


# Must contain this color in text
def hextotext(i, password):
    # Setup choices
    choices = []
    if color_choice == "FF0000":
        choices = ["red"]
    elif color_choice == "00FF00":
        choices = ["green"]
    elif color_choice == "00FF00":
        choices = ["blue"]
    elif color_choice == "FFFF00":
        choices = ["yellow"]
    elif color_choice == "00FFFF":
        choices = ["cyan", "turquoise"]
    elif color_choice == "FF00FF":
        choices = ["magenta", "purple", "pink", "lilac", "violet"]
    # For each choice test if it is in password
    for color in choices:
        if color in password.lower():
            return True
    # Did not pass
    print(
        "Rule "
        + str(i)
        + ": Password must include the name of the color #"
        + color_choice
        + " (That is hexadecimal rgb)."
    )
    return False

# Random history based dates
import random

# Generate random persistent values
important_date = random.choice(
    [
        {"name": "of the Battle of Hastings.", "date": "1066"},
        {"name": "of the Sealing of the Magna Carta.", "date": "1215"},
        {"name": "when the Black Death arrived in england.", "date": "1346"},
        {"name": "when the War of the Roses begins.", "date": "1455"},
        {"name": "when Shakespeare was Born.", "date": "1564"},
        {"name": "of the Discovery of the Gunpowder Plot.", "date": "1605"},
        {"name": "of the Battle of Waterloo.", "date": "1815"},
        {"name": "when Queen Victoria became Queen.", "date": "1837"},
        {"name": "when World War 2 Ended.", "date": "1945"},
        {"name": "when the World Wide Web was Invented.", "date": "1989"},
    ]
)


# Random date
def date(i, password):
    # Check if year is in password
    if important_date["date"] in password:
        return True
    # Did not pass
    print(
        "Rule " + str(i) + ": Password must contain the year " + important_date["name"]
    )
    return False

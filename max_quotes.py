import random
import datetime

# Load quotes from a file
with open("quotes.txt", "r") as f:
    quotes = f.readlines()

# Select a random quote
daily_quote = random.choice(quotes).strip()

# Write the quote to a log file with today's date
with open("updates/log.txt", "a") as log:
    log.write(f"{datetime.date.today()}: {daily_quote}\n")

print("Daily quote added!")

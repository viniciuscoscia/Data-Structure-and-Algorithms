import csv
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    unique_numbers = set()
    for text in texts:
        unique_numbers.add(text[0])
        unique_numbers.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        unique_numbers.add(call[0])
        unique_numbers.add(call[1])

print("There are " + str(len(unique_numbers)) + " different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

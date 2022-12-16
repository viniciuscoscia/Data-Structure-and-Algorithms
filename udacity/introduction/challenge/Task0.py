import csv

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_record = texts[0]
    print("First record of texts, " + first_record[0] + " texts " + first_record[1] + " at time " + first_record[2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call = calls[len(calls) - 1]
    print("Last record of calls, " + last_call[0] + " calls " + last_call[1] + " at time " + last_call[2] + ", lasting " + last_call[3] + " seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

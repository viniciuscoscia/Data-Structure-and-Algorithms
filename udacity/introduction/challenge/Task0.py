import csv

"""
 Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0.
  Example: "(022)40840621".
 Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. 
 The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
 Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".
"""
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

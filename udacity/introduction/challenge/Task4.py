"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

possible_telemarketers = set()
false_flags = set()

for call in calls:
    origin = str(call[0])
    destination = str(call[1])

    possible_telemarketers.add(origin)
    false_flags.add(destination)

for false_flag in false_flags:
    possible_telemarketers.discard(false_flag)

for text in texts:
    origin = str(text[0])
    destination = str(text[1])

    possible_telemarketers.discard(origin)
    possible_telemarketers.discard(destination)

print("These numbers could be telemarketers: ")
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


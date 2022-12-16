"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def is_mobile_number(number):
    return number.startswith("7") or number.startswith("8") or number.startswith("9")


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    codes = set()
    bangalore_origin_calls = 0
    bangalore_destination_calls = 0

    for call in calls:
        caller_number = call[0]

        if not caller_number.startswith("(080)"):
            continue

        bangalore_origin_calls += 1
        destination_number = str(call[1])

        if destination_number.startswith("("):
            prefix = destination_number.split(")")[0].replace("(", "")
            if prefix == '080':
                bangalore_destination_calls += 1
            codes.add(prefix)
        elif is_mobile_number(destination_number):
            codes.add(destination_number[0:4])

print("The numbers called by people in Bangalore have codes:")
print(codes)

calls_percentage = (bangalore_destination_calls * 100) / bangalore_origin_calls

print(
    f"{round(calls_percentage, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in "
    f"Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

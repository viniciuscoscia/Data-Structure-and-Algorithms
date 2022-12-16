"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv


def add_call_duration(phone_number, duration):
    if phone_total_call_times.get(phone_number) is None:
        phone_total_call_times[phone_number] = 0

    phone_total_call_times[phone_number] += duration


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    number_spent_longest_time = str('')
    longest_call_duration_sum = 0
    phone_total_call_times = dict()

    for call in calls:
        calling_telephone_number = call[0]
        receiving_telephone_number = call[1]
        call_duration = int(call[3])

        add_call_duration(calling_telephone_number, call_duration)
        if phone_total_call_times[calling_telephone_number] > longest_call_duration_sum:
            longest_call_duration_sum = phone_total_call_times[calling_telephone_number]
            number_spent_longest_time = calling_telephone_number

        add_call_duration(receiving_telephone_number, call_duration)
        if phone_total_call_times[receiving_telephone_number] > longest_call_duration_sum:
            longest_call_duration_sum = phone_total_call_times[receiving_telephone_number]
            number_spent_longest_time = receiving_telephone_number

print(
    f'{number_spent_longest_time} spent the longest time, {longest_call_duration_sum} seconds, on the phone during '
    f'September 2016.')

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

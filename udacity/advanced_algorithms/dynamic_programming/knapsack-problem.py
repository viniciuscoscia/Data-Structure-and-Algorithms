# Helper code
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


def knapsack_max_value(knapsack_max_weight, items: list[Item]):
    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:
        # The "capacity" represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)
            else:
                break

    return lookup_table[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [
                    Item(weight=10, value=7),
                    Item(weight=9, value=8),
                    Item(weight=5, value=6)
                ]
            }
    },
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [
                    Item(weight=10, value=2),
                    Item(weight=29, value=10),
                    Item(weight=5, value=7),
                    Item(weight=5, value=3),
                    Item(weight=5, value=1),
                    Item(weight=24, value=12)
                ]
            }
    }
]

for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])

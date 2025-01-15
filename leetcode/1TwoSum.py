from collections import defaultdict
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = defaultdict(list)
    for i in range(len(nums)):
        d[nums[i]].append(i)

    for value, indexes in d.items():
        print(value, indexes)
        required_value = target - value

        if required_value == value and len(indexes) > 1:
            return [indexes[0], indexes[1]]
        elif required_value in d and value != required_value:
            return [indexes[0], d[target - value][0]]

# Claude AI
def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in nums that add up to target and return their indices.

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List containing indices of two numbers that add up to target

    Example:
        >>> Solution().twoSum([2,7,11,15], 9)
        [0,1]
        >>> Solution().twoSum([3,3], 6)
        [0,1]
    """
    seen = {}  # val -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  # No solution found
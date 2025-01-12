from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_numbers = set()
        for number in nums:
            if number not in unique_numbers:
                unique_numbers.add(number)
            else:
                unique_numbers.remove(number)

        return unique_numbers.pop()
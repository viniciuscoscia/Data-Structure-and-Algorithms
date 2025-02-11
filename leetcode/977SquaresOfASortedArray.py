from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right_pointer = len(nums) - 1
        left_pointer = 0
        index = 0
        result = [None] * len(nums)

        while right_pointer > left_pointer:
            left_number = abs(nums[left_pointer])
            right_number = abs(nums[right_pointer])

            if left_number > right_number:
                result[index] = left_number * left_number
                left_pointer += 1
            else:
                result[index] = right_number * right_number
                right_pointer += 1

            index -= 1

        return result
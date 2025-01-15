from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        real_rotations = k % len(nums)
        temp_list = [None] * length

        for i in range(len(nums)):
            new_position = real_rotations + i

            if new_position >= length:
                new_position = real_rotations + i - length

            temp_list[new_position] = nums[i]

        for index, e in enumerate(temp_list):
            nums[index] = e

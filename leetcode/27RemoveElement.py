from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_index = 0
        end_index = len(nums)

        while start_index < end_index:
            if nums[start_index] == val:
                end_index -= 1
                nums[start_index] = nums[end_index]
            else:
                start_index += 1
        return end_index

# print(Solution().removeElement([2], 3))
print(Solution().removeElement([1], 1))
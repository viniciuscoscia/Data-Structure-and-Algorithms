from typing import List


def removeDuplicates(nums: List[int]) -> int:
    x = 0
    for i in range(1, len(nums)):
        if nums[x] != nums[i]:
            x += 1
            nums[x] = nums[i]

    print(nums)
    return x

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([1,1,2]))
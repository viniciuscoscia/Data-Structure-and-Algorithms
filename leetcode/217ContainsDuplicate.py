from operator import truediv
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                return True
        return False


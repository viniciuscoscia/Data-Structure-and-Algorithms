from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1:
            return derived[0] == 0

        original = [0]

        for i in range(len(derived) - 1):
            next_val = original[i] ^ derived[i]
            original.append(next_val)

        return (original[-1] ^ original[0]) == derived[-1]
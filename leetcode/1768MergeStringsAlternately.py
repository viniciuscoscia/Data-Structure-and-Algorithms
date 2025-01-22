class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        result = ""
        for i in range(min_length):
            result = result + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]

        return result + word1 + word2


print(Solution().mergeAlternately("abc", "pqr"))
print(Solution().mergeAlternately("abcd", "pq"))
print(Solution().mergeAlternately("ab", "pqrs"))
print(Solution().mergeAlternately("Vnicius", "i"))
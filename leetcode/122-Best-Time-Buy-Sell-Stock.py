from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        index = 0

        while index < len(prices) - 1:
            while index < len(prices) - 1 and prices[index] > prices[index + 1]:
                index += 1
            buy_value = prices[index]

            while index < len(prices) - 1 and prices[index] < prices[index + 1]:
                index += 1
            sell_value = prices[index]

            profit += sell_value - buy_value

        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
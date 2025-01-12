from typing import List



def maxProfit( prices: List[int]) -> int:
    profit = 0
    current_stock_index = 0
    for index in range(1, len(prices) - 1):
        if prices[current_stock_index] >= prices[index]:  # If the next stock is cheaper, let's go for it
            current_stock_index += 1
        elif prices[index + 1] < prices[index]: # The next stock is more expensive, then sell it
            profit += prices[index] - prices[current_stock_index]
            current_stock_index = index
        elif index == len(prices) - 1 and prices[current_stock_index] < prices[index]:
            profit += prices[index] - prices[current_stock_index]

    return profit



print(maxProfit([1,2,3,4,5]))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         current_stock_index = 0
#         for index in range(1, len(prices) - 1):
#             if prices[current_stock_index] >= prices[index]:  # If the next stock is cheaper, let's go for it
#                 current_stock_index += 1
#             elif prices[index + 1] < prices[index]: # The next stock is expensiver, then sell it
#                 profit += prices[index] - prices[current_stock_index]
#                 current_stock_index = index
#             elif index == len(prices) - 1 and prices[current_stock_index] < prices[index]:
#                 profit += prices[index] - prices[current_stock_index]
#
#         return profit

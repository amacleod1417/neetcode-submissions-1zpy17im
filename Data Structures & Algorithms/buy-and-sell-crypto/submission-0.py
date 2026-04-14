class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        i = 1

        while i < len(prices):

            profit = prices[i] - min(prices[:i])

            if profit > max_profit:
                max_profit = profit

            i += 1
            
        return max_profit

            
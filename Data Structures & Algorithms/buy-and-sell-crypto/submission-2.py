class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        min_price = prices[0]
        total_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                total_profit = max(total_profit, profit)
        return total_profit
        


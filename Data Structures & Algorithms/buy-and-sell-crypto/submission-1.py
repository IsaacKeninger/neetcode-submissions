class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        total_profit = 0

        for price in prices[1:]:# start from first index
            if price < min_price:
                min_price = price # new best day to buy
            else:
                profit = price - min_price
                total_profit = max(total_profit, profit)
                
        return total_profit


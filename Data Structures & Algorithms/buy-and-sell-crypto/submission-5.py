class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1
        total_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                highest = prices[r] - prices[l]
                total_profit = max(highest, total_profit)
            else:
                l = r
            r += 1
        return total_profit
        
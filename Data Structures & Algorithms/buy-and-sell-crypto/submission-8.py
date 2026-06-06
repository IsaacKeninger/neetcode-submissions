class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l,r = 0, 1

        while r < len(prices):
            curr = 0
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                max_profit = max(curr, max_profit)
            else:
                l = r
            r += 1
        return max_profit
                
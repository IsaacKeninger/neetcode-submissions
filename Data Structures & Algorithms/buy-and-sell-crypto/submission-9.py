class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        max_profit = 0
        l,r = 0,1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                curr = prices[r] - prices[l]
                max_profit = max(curr, max_profit)
            r += 1
        return max_profit






class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0
        l = 0
        for r in range(len(prices)):
            if l < r and prices[l] < prices[r]:
                best = max(best, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return best
        
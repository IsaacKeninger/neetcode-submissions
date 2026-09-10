class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                best = max(prices[r] - prices[l], best)
        return best
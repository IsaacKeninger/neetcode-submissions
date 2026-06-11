class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0 
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
            else:
                l = r
            r += 1
        return maxProfit



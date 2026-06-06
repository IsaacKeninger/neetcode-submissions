class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            # profitable or not
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

            
        return maxP

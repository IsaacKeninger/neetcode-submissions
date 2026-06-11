class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]: # there is a profit to be found
                res = max(res, (prices[r] - prices[l]))
            else:
                l = r
            r += 1 
        return res
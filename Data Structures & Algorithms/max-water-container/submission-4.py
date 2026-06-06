class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAmt = 0

        while l < r:
            width = r - l
            h = min(heights[r], heights[l])
            maxAmt = max(maxAmt, width * h)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
        return maxAmt
                
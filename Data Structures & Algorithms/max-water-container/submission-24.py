class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        best = min(heights[r], heights[l]) * (r - l)
        while l < r:
            val = min(heights[r], heights[l]) * (r - l)
            best = max(best, val)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best
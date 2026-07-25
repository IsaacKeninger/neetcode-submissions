class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area of 2 bars = min(heights[l], heights[r]) * (r - l)
        l,r = 0, len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (r - l)
        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, currArea)
        return maxArea


        
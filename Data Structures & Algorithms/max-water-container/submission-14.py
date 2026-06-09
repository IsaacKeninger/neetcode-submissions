class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(height) * width

        l,r = 0, len(heights)-1
        best = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            best = max(best, area)

        return best

        
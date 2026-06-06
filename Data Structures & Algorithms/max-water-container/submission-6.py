class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l,r = 0, len(heights)-1

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            curr_area = w * h
            max_area = max(curr_area, max_area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
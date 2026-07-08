class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = max(val1, val2) * (r - l)

        l,r = 0, len(heights) - 1
        res = min(heights[l], heights[r]) * (r-l)
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


        

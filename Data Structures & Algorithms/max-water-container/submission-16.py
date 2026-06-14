class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights)-1
        res = min(heights[r], heights[l]) * (r - l)

        while l < r:
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            res = max(res, min(heights[r], heights[l]) * (r - l))
        return res

        
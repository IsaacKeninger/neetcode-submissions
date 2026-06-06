class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res = (r-l) * min(heights[r], heights[l]) 

        while l < r:
            curr = (r-l) * min(heights[r], heights[l])
            res = max(curr, res)
            
            if heights[l] <= heights[r] and l < r:
                l += 1
            else:
                r -= 1
        return res

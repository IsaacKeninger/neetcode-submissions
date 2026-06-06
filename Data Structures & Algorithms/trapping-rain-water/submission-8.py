class Solution:
    def trap(self, height: List[int]) -> int: 

        # invariant: min(height[r], height[l]) - height[i]

        max_area = 0    
        l,r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]

        while l < r:

            if lMax < rMax:
                l += 1
                lMax = max(height[l], lMax)
                max_area += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r], rMax)
                max_area += rMax - height[r]
            
        return max_area

        
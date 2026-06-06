class Solution:
    def trap(self, height: List[int]) -> int:
        """
        arr of ints >= 0 (height)
        returning maxium area of water that can be trapped between bars
        """
        # we know that min(leftMax, rightMax) - height[i] is the amt of water trapped 
        # because lower side constrains the column

        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        maxArea = 0

        while l < r: # O(n)
            if lMax < rMax:
                l += 1
                lMax = max(height[l], lMax)
                maxArea += lMax - height[l]
            else:
                r -= 1
                rMax = max(height[r], rMax)
                maxArea += rMax - height[r]
            
        return maxArea

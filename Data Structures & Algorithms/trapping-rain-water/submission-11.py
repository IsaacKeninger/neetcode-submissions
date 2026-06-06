class Solution:
    def trap(self, height: List[int]) -> int:
        # invariant: min(heights[l], heights[r]) - heights[i]

        l,r = 0, len(height) - 1
        best = 0
        leftmax,rightmax = height[l], height[r]

        while l < r:
            if height[l] > height[r]:
                r -= 1
                rightmax = max(rightmax, height[r])
                best += rightmax - height[r]
            else:
                l += 1
                leftmax = max(leftmax, height[l])
                best += leftmax - height[l]
        return best
            

            

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        arr of ints >= 0 (height)
        returning maxium area of water that can be trapped between bars
        """
        # we know that min(leftMax, rightMax) - height[i] is the amt of water trapped 
        # because lower side constrains the column

        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l] # add to the res: height of left barrier minus heigh of boxa head of it
            else: # rmax is bigger or equal to
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res
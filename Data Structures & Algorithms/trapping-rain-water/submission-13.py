class Solution:
    def trap(self, height: List[int]) -> int:

        l,r = 0, len(height)-1
        Lmax,rMax = height[l], height[r]
        res = 0

        while l < r:

            if Lmax < rMax:
                l += 1
                Lmax = max(Lmax, height[l])
                res += Lmax - height[l]
            else:
                        r -= 1
                        rMax = max(rMax, height[r])
                        res += rMax - height[r]
        return res
        
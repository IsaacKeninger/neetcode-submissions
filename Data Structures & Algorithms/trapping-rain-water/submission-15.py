class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1
        L,R = height[l], height[r]

        while l < r:
            if L < R:
                l += 1
                L = max(height[l], L)
                res += L - height[l]
            else:
                r -= 1
                R = max(height[r], R)
                res += R - height[r]
        return res
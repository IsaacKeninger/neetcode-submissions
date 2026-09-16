class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return the minimum elem
        l,r = 0, len(nums) - 1
        
        # if middle value > rightmost value, we know that the min is to the right
        while l < r:
            m = (l + r) // 2 # midpoint
            if nums[m] > nums[r]: # we know that the min is to the right
                l = m + 1
            else:
                r = m
        return nums[l]

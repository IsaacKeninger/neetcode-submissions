class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a fixed point
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            if a > 0:
                break # there are no more triplets
            
            l,r = i + 1, len(nums)-1
            while l < r:
                val = nums[l] + nums[r] + a
                if val < 0: l += 1
                elif val > 0: r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        # do 2 pointers to find triplet
        return res
        
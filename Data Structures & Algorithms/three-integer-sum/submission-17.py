class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort it 
        res = []

        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]: # if its a duplicate 
                continue
            
            l,r = i+1, len(nums)-1
            while l < r:
                curr = e + nums[l] + nums[r]
                
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([e, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
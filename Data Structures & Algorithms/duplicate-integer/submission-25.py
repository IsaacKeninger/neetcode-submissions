class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        map = set()

        for i in range(len(nums)):
            if nums[i] in map:
                return True
            else:
                map.add(nums[i])
                
        return False
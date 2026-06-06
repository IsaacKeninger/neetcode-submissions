class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for item in nums:
            if item not in nums2:
                nums2.append(item)
            else:
                return True
        return False

         
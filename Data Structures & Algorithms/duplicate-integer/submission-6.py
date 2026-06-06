class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = []

        for item in nums:
            if item not in map:
                map.append(item)
            else:
                return True

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for char in nums:
            if char in seen:
                return True
            seen.add(char)
        return False
        
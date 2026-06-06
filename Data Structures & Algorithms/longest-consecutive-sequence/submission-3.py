class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset:
                j = 1
                while num + j in numset:
                    j += 1
                longest = max(j, longest)
        return longest
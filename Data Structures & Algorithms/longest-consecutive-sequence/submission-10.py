class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        best = 0

        for num in numset:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                best = max(length, best)
        
        return best
        
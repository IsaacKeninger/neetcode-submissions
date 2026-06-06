class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        best = 0
        for num in nums:
            if num - 1 not in numset: # meaning its start of a seq
                length = 1
                while num + 1 in numset:
                    num += 1
                    length += 1
                best = max(best, length)
        return best
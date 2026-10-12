class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0

        for num in numset:
            if num - 1 not in numset: # starting point
                curr_length = 1
                while num + curr_length in numset:
                    curr_length += 1
                longest = max(longest, curr_length)
        
        return longest

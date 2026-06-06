class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        best = 1
        hm = set(nums)

        # head if nums[i] - 1 not in hm
        for num in hm:
            if num - 1 not in hm:
                length = 1
                curr = num
                while curr + 1 in hm:
                    length += 1
                    curr += 1
                best = max(best, length)
        return best
                 


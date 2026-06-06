class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = 1
        numset = set(nums)

        for num in numset:
            if num - 1 not in numset:
                length = 1
                curr = num
                while curr + 1 in numset:
                    length += 1
                    curr += 1
                best = max(best, length)
        return best
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:\

        best = 0
        numset = set(nums)

        for num in numset:
            if num - 1 not in numset: # head
                curr = num
                long = 1

                while curr + 1 in numset:
                    long += 1
                    curr += 1
                best = max(best, long)
        return best

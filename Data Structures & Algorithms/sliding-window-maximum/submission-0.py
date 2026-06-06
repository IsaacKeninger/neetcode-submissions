class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        GIVEN: nums (arr int), k (int)
        RESULT: max of sliding window each iteration
        """

        res = []

        for i in range(len(nums) - k + 1):
            maxI = nums[i]
            for j in range(i, i +k):
                maxI = max(maxI, nums[j])
            res.append(maxI)
        return res
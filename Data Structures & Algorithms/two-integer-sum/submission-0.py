class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        given: nums (arr(ints)), target (int)
        doing: iterate through the list, checking if 2 indices add up to target
        returning: indices of 2 numbers adding to target
        """
        # Upper Bound = O(n)

        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i    
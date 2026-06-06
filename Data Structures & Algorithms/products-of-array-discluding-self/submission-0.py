class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        given: nums(int arr)
        doing: appending to answer product of all values except nums[i] in the loop
        return: answer(arr)
        """

        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        n = len(nums)
        postfix = 1
        for i in range(n-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
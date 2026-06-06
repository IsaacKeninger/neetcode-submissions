class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        given: nums(int arr)
        doing: appending to answer product of all values except nums[i] in the loop
        return: answer(arr)
        """
        n = len(nums)
        res = [1] * n

        pre=1
        suf=1

        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        for i in range(n-1,-1,-1):
            res[i] *= suf
            suf *= nums[i]
        return res
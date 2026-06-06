class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given: nums(arr)
        # doing: check if any value appears at least twice or not
        # returning: True if yes (a value appears 2+ times), False if no (each value it distinct)

        # # naive solution
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
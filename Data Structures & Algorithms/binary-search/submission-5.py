class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0, len(nums) - 1 # start at beginning and end of list

        while low <= high: # while the left index is less than or equal to the right, still in confines of unchecked list
            midpoint = low + (high - low) // 2 # 0 + (6) = 6 // 2 = 3 
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                high = midpoint - 1
            else:
                low = midpoint + 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = high - (high - low) // 2 # calculate midpoint

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        
        return -1 # target not found

            


        
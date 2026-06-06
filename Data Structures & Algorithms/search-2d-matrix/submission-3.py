class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this idea joins the 2 arrays into 1 list then does serach
        combined = []
        for arr in matrix: # O(m) part
            combined += arr
        
        l,r = 0, len(combined) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if combined[mid] == target:
                return True
            elif combined[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
        
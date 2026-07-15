class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [item for row in matrix for item in row]
        l,r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
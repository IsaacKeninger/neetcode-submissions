class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        given: numbers (int arr)
        returning: indices of 2 numbers, that add up to targetand index1 < index2
        """

        n = len(numbers)
        p1 = 0

        while p1 < n - 1:
            p2 = p1 + 1
            while p2 < n:
                if numbers[p1] + numbers[p2] == target:
                    return [p1+1, p2+1]
                p2 += 1
            p1 += 1

            
        
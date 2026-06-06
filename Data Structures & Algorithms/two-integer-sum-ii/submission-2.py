class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        given: numbers (int arr)
        returning: indices of 2 numbers, that add up to targetand index1 < index2
        """

        n = len(numbers)
        p1, p2 = 0 , n - 1

        while p1 < p2:
            curr_sum = numbers[p2] + numbers[p1]
            if curr_sum == target:
                return [p1+1, p2+1]
            elif curr_sum < target:
                p1 += 1
            else:
                p2 -= 1

            
        
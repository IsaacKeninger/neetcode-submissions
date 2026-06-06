class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ 
        given: temperatures (arr int)
        return: result (arr)
        """
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result
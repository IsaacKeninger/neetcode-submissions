class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ 
        given: temperatures (arr int)
        return: result (arr)
        """
        result = [0] * len(temperatures)
        stack = []

        # pattern | monotonic decreasing stack
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]: # while temp adding is greater keep monoticity
                t_idx, t_val = stack.pop()
                result[t_idx] = idx - t_idx
            stack.append((idx, temp))
        return result
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ 
        given: temperatures (arr int)
        return: result (arr)
        """
        result = [0] * len(temperatures)
        stack = []

        # monotonic decreasing stack | ALWAYS DECREASING IN ORDER
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop() # pop from stack
                result[stackIdx] = (i - stackIdx)
            stack.append((temp, i))
        return result
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                valTemp, valIdx = stack.pop()
                result[valIdx] = idx - valIdx
            stack.append((temp, idx))
        return result
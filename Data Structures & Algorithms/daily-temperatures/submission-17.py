class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                valIdx, valTemp = stack.pop()
                res[valIdx] = i - valIdx
            stack.append((i, t))
        return res
            
        
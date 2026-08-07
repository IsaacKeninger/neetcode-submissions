class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                poppedIdx, poppedTemp = stack.pop()
                res[poppedIdx] = i - poppedIdx
            else:
                stack.append((i, t))
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                vT, vI = stack.pop()
                res[vI] = i - vI
            stack.append((t,i))
        return res
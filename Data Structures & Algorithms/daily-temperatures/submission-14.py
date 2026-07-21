class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack, means it must decrease
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                vT, vI = stack.pop()
                res[vI] = idx - vI
            stack.append((temp, idx))
        return res
                
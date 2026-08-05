class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        # must be decreasing at all times, monotonic
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                v_idx, v_temp = stack.pop()
                res[v_idx] = i - v_idx
            stack.append((i, t))
        
        return res
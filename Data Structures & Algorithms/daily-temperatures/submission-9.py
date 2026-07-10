class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        stack = []
        result = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                v_temp, v_idx = stack.pop()
                result[v_idx] = idx - v_idx
            stack.append((temp, idx))
        return result
        
            

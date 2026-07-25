class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotonic stack
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                vT, vI = stack.pop()
                result[vI] = i - vI
            stack.append((t,i))
        return result

                

            
        
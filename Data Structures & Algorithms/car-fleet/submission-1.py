class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the pairs into 1 sorted array [(p, s), (p, s)]
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



        
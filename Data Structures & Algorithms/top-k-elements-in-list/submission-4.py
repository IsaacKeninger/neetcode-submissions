class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {} # (val : freq)
        final = []
        for num in nums:
            res[num] = 1 + res.get(num, 0)

        res = sorted(res.items(), key=lambda items:items[1], reverse=True)

        for i in range(len(res)):
            final.append(res[i][0])
            if len(final) == k:
                return final

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            ctr[num] = 1 + ctr.get(num, 0)
        ctrSortedByKey = sorted(ctr.keys(), key=lambda x:ctr[x], reverse=True)

        return ctrSortedByKey[:k]
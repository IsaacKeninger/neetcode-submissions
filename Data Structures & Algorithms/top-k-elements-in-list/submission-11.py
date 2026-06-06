class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        hm_sortedbykey = sorted(hm.keys(), key=lambda x:hm[x], reverse=True)

        return hm_sortedbykey[:k]
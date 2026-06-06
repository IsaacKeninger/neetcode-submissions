class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums:
            hm[num] = 1 + hm.get(num, 0) # {1: 1, 2:2, 3:3} k = 2

        hm_sorted = sorted(hm.keys(),key=lambda occ:hm[occ], reverse=True)
        # {3:3, 2:2, 1:1}

        return hm_sorted[:k]
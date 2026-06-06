class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make counter
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        # sort by key

        hm_sortbykey = sorted(hm.keys(), key=lambda x:hm[x], reverse=True)
        
        return hm_sortbykey[:k]

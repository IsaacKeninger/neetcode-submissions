class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements in the arr
        hm = {}

        # make counter
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        hm_sorted = sorted(hm.keys(),key=lambda x:hm[x],reverse=True)

        return hm_sorted[:k]
        
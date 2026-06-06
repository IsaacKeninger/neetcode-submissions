class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        bucket_sort = sorted(hm.keys(), key=lambda x:hm[x],reverse=True)

        return bucket_sort[:k]
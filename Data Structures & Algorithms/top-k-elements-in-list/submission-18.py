class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        hm_sort = sorted(hm.items(), key=lambda x:x[1], reverse=True)

        return [item[0] for item in hm_sort[:k]]

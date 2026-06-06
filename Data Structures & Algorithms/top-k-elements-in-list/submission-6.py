class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket sort

        hm = {}
        res = []
        
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        hm_sorted = sorted(hm.items(), key=lambda items:items[1], reverse=True)

        for i in range(len(hm_sorted)):
            res.append(hm_sorted[i][0])
            if len(res) == k:
                return res
        return res
    
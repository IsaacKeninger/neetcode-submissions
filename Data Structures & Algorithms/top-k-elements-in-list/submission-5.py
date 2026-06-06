class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}
        res = []

        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        sorted_hm = sorted(hm.items(), key=lambda items:items[1], reverse=True)

        for i in range(len(sorted_hm)):
            res.append(sorted_hm[i][0])
            if len(res) == k:
                return res
        
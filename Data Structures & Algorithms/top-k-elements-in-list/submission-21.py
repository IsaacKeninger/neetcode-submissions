class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        hm = sorted(hm.items(), key=lambda x:x[1], reverse=True)    

        res = []
        for i in range(k):
            res.append(hm[i][0])
        
        return res
            
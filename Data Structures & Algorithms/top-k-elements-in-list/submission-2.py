class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sorted_count = sorted(count.items(), key=lambda items:items[1], reverse=True)

        for i in range(len(sorted_count)):
            res.append(sorted_count[i][0])
            if len(res) == k:
                return res

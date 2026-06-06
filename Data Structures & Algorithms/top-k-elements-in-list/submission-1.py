class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        res = []

        for i in range(len(nums)):
            freqs[nums[i]] = 1 + freqs.get(nums[i], 0)
        
        sorted_freqs = sorted(freqs.items(), key=lambda items:items[1], reverse=True)

        for i in range(len(sorted_freqs)):
            res.append(sorted_freqs[i][0])
            if len(res) == k:
                return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(hashmap[i][0])
        
        return result
        
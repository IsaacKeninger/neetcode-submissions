class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        # {num: occ}

        hm_sortByOcc = sorted(hm.items(), key=lambda x:x[1], reverse=True)

        res = []
        for item in hm_sortByOcc:
            res.append(item[0])

        return res[:k]
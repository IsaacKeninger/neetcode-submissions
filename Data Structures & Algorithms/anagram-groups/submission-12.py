class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            fmap = [0] * 26
            for c in s:
                p = ord(c) - ord('a')
                fmap[p] += 1
            res[tuple(fmap)].append(s)
        return list(res.values())
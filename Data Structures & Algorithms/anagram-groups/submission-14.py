class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            fmap = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                fmap[pos] += 1
            hm[tuple(fmap)].append(s)
        return list(hm.values())

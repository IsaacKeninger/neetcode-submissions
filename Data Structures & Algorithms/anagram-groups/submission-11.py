class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freqmap = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                freqmap[pos] += 1
            res[tuple(freqmap)].append(s)
        return list(res.values())
        
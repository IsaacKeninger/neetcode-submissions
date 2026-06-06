class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                freq[pos] += 1
            res[tuple(freq)].append(s)
        return list(res.values())
            
        
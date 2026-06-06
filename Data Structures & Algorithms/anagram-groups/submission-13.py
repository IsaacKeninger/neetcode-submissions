class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            fMap = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                fMap[pos] += 1
            res[tuple(fMap)].append(s)
        return list(res.values())
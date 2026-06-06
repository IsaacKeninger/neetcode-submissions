class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                freq[pos] += 1
            hm[tuple(freq)].append(s)
        
        return list(hm.values())

        
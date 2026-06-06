class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # representation of chars in each str
        # if that representation is the same as another, group it together

        res = defaultdict(list)

        for s in strs:
            freqMap = [0] * 26 # represent characters in alphabet
            for c in s:
                # find position of character
                pos = ord(c) - ord('a')
                freqMap[pos] += 1
            res[tuple(freqMap)].append(s)
                
        return list(res.values())
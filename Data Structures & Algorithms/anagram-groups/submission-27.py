class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            frequency_map = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                frequency_map[pos] += 1
            result[tuple(frequency_map)].append(s)
        
        return list(result.values())
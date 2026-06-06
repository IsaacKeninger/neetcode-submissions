class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + '#' + s)
        return res
    # 5#hello#world
    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            content = s[j + 1: j + 1 + length]
            decoded_strs.append(content)
            i = j + 1 + length

        return decoded_strs;

        







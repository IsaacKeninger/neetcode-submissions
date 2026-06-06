class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        #find delimeter
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            i = j + 1

            strs.append(s[i:i+length])
            i += length

        return strs

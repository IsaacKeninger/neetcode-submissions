class Solution:
    """
    given: list of strs (strs)
    doing: encoding into a single string, then decoding back into list of strs
    return: list of strs (same as input)
    """

    def encode(self, strs: List[str]) -> str:
        # ex "5#hello5#world"
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))
            encoded_string += '#'
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = s.index('#', i)        # built-in C-speed scan from position i
            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return strs

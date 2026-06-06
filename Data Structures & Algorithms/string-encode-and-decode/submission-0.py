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
            j = i
            while s[j] != '#': #checks right in front of i
                j += 1
            
            # Everything from i to j is the length prefix
            length = int(s[i:j]) # takes number val
            
            # Slice exactly `length` chars after the '#'
            strs.append(s[j + 1 : j + 1 + length]) # slice the length characters
            
            # Move i to the start of the next encoded entry
            i = j + 1 + length # move i to start of next entry

        return strs

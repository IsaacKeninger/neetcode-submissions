class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            l = 0
            best = 0

            for r in range(len(s)):

                count[s[r]] = 1 + count.get(s[r], 0)
                # invariant: size of window - max(freq_elems) > k
                while r-l+1 - max(count.values()) > k:
                    # shrink window
                    count[s[l]] -= 1
                    l += 1
            
                best = max(r-l+1, best)
            return best
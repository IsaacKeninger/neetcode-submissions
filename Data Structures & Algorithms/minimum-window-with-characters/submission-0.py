from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        # Frequency of chars needed
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Window state
        l, r = 0, 0
        formed = 0 # How many unique chars meet the required freq
        window_counts = {}
        
        # (length, left, right)
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the frequency of the current char matches the requirement
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try to shrink the window from the left
            while l <= r and formed == required:
                char = s[l]
                
                # Update result if this is the smallest window yet
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove char at 'l' and update formed count
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1    

            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

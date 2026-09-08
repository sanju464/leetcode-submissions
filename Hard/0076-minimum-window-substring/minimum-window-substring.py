class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
        
        # Build frequency map for string t manually
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
            
        missing = len(t)
        left = 0
        min_start = 0
        min_len = float('inf')
        
        for right, char in enumerate(s):
            # If current character is needed, decrease missing count
            if char in need and need[char] > 0:
                missing -= 1
            
            # Decrement frequency count
            need[char] = need.get(char, 0) - 1
            
            # When all characters from 't' are satisfied
            while missing == 0:
                # Track smallest window length and start index
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Shrink window from the left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1  # Lost a required character
                left += 1
                
        return "" if min_len == float('inf') else s[min_start : min_start + min_len]
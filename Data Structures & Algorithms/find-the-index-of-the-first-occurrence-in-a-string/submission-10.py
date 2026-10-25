class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        # Loop through each possible starting position
        for i in range(n - m + 1):
            # Check if the slice matches the needle
            if haystack[i:i + m] == needle:
                return i
                
        return -1
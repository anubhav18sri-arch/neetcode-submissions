class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for string s
        j = 0  # Pointer for string t
        
        # Traverse through both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for s forward
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for t forward
            j += 1
            
        # If we successfully matched every character in s, i will equal len(s)
        return i == len(s)
        
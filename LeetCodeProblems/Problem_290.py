"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s."""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False        
        for i in range (len(s)):
            if pattern.find(pattern[i]) != s.index(s[i]):
                return False
        return True

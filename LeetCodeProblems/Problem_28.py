"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:       
        hs = len(haystack)
        nd = len(needle) 
        if hs < nd: 
            return -1      
        if hs == nd:
            if haystack == needle:
                return 0
            else:
                return -1       
        for i in range(hs - nd + 1):
            if haystack[i : i + nd] == needle:
                return i       
        return -1

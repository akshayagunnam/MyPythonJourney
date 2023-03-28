"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ''
        if strs[0] == '': 
            return ''

        result, c = strs[0][0], 1
        
        while c <= len(strs[0]):
            for i in strs:
                if result != i[:len(result)]:
                    return result[:-1]
            if c >= len(strs[0]):
                break
            result += strs[0][c]
            c += 1
            
        return result
            

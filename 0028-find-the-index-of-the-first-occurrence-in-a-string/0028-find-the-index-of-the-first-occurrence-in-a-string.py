class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            else:
                return -1
        else:
            for i in range((len(haystack)-len(needle))+1):
                if haystack[i:len(needle)+i] == needle:
                    return i

        return -1
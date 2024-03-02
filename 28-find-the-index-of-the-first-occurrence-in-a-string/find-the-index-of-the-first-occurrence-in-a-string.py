#Intution is to create a sliding window of length equal to the needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        elif len(needle) > len(haystack):
            return -1
        else: 
            for i in range(0, len(haystack)-len(needle)+1):
                if needle == haystack[i:i+len(needle)]:
                    return i
            return -1
                

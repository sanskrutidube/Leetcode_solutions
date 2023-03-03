class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m,n=len(haystack),len(needle)
        for i in range(m):
            if haystack[i:i+n]==needle: return i
        return -1
------------------------------------------------------------

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
	
        x = len(haystack)
        l = len(needle)
        if haystack==needle:
            return 0
        if x==0 and l==0:
            return 0
        for i in range(0,x-l+1):
            if haystack[i:i+l]==needle:
                return i
        return -1
	

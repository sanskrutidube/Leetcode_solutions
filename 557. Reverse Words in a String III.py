class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        words = s.split()
        for word in words:
            ans += word[::-1]
            ans += ' '

        return ans[:-1]
------------------------------------------------------

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]    

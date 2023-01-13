class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        ans = 0
        for i in range(len(s)):
            s[i] = s[i].count(' ') + 1
            ans = max(ans, s[i])
        return ans
       
       
--------------------------------------------------------------

class Solution(object):
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(word.split()) for word in sentences)
        
        
------------------------------------------------------------
class Solution(object):
    def mostWordsFound(self, sentences):
        res = 0
        lst =[]
        for i in sentences:
            lst = i.split(" ")
            res = max(res,len(lst))
            lst = []
        return res
        

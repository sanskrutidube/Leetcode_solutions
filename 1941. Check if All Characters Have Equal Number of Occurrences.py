class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
        
        
 ------------------------------------------------------
 
 class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(collections.Counter(s).values()))==1
        
 -----------------------------------------------------------
 
 class Solution(object):
    def areOccurrencesEqual(self, s):
        lis =[]
        for i in s:
            lis.append(s.count(i))
        if len(set(lis))==1:
            return True
        return False

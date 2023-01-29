class Solution(object):
    def commonFactors(self, a, b):
        count = 0
        for i in range(1,min(a,b)+1):
            if a % i == 0 and b % i == 0 :count=count+1
        return count
-------------------------------------------------------------

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        l=[]
        for i in range(1,min(a,b)+1):
            if a % i ==0  and b % i ==0:
                l.append(i)
        return len(l)
        
        

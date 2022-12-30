class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l = [1]
        while l[-1]<n:
            l.append(3**len(l))
        for i in l[::-1]:
            if i <= n:
                n -= i
        return n==0
        
        
--------------------------------------------------------------

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while (n>=1):
            if n%3==2: return False
            n=n//3
        return True
            

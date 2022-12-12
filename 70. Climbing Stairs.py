class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,1]
        for i in range(n-1):
            a.append(a[-1]+a[-2])
        return a[n]
        
-------------------------------------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n<2):
            return n
        count=[1,2]
        for i in range(2,n):
            count.append(count[i-1]+count[i-2])
        return count[n-1]
--------------------------------------------------------

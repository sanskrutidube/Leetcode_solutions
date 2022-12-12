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
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in xrange(n)]
    res[0], res[1] = 1, 2
    for i in xrange(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]
--------------------------------------------------------
class Solution:
    def climbStairs(self, n):
        if n == 1:
           return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
           res[i] = res[i-1] + res[i-2]
        return res[-1]
---------------------------------------------------------
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in xrange(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b

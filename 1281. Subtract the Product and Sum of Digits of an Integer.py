class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return prod(list(map(int,str(n))))-sum(list(map(int,str(n))))
-----------------------------------------------------------------------

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p,s=1,0
        while n!=0:
            p*=(n%10)
            s+=(n%10)
            n//=10
        return p-s
--------------------------------------------------------------------------

import numpy as np

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return np.prod(a) - np.sum(a)
        
---------------------------------------------------------------------------

class Solution(object):
    def subtractProductAndSum(self, n):
        sn = str(n)
        sum =0
        pro=1
        for i in sn:
            sum=sum+int(i)
            pro = pro*int(i)
        return pro-sum

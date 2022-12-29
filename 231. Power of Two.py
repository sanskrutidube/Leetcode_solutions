class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0 or n == 0:
            return False
        return self.isPowerOfTwo(n/2)
      
---------------------------------------------------------

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        while (n%2==0):
            n=n/2
        return n==1

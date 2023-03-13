class Solution:
    def numSquares(self, n):
        sqr = sqrt(n)
        pool = {i**2 for i in range(int(sqr)+1)}
        test = [i**2 for i in range(int(sqr*0.71)+1)]
        
        for i in test:
            for j in test:
                if n-i-j in pool:
                    return 3-(i==0)-(j==0)
        return 4

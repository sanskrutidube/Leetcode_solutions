class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [0] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return ans
        
---------------------------------------------------------------------------

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False 
        for number in range(2, n):
            if primes[number]:
                for multiple in range(2 * number, n, number):
                    primes[multiple] = False
        return sum(primes)
	

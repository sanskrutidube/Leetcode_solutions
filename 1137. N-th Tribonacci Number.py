class Solution:
    def tribonacci(self, n: int) -> int:
    	a, b, c = 0, 1, 1
    	for i in range(n): a, b, c = b, c, a + b + c
    	return a
		
-------------------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        lst = [0, 1, 1]
        if n < 2:
            return lst[n]
        else:            
            for i in range(n-2):
                lst.append(sum(lst))
                lst.pop(0)
        return lst.pop()

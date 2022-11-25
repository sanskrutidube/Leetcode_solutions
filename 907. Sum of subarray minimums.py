class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = (10 ** 9) + 7
        stack = []
        dp = [0] * len(arr)
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] >= n:
                stack.pop()

            if stack:
                dp[i] = dp[stack[-1]] + (n * (i - stack[-1]))
            
            else:
                dp[i] = n * (i + 1)

            stack.append(i)

        return sum(dp) % mod
      
  ----------------------------------------------------------------
  
  class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = [] # monotonically increasing stack
        ans = 0
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                prevIdx = stack.pop()
                right = i - prevIdx - 1
                left = prevIdx if not stack else prevIdx - stack[-1] - 1
                ans +=  arr[prevIdx]* (1 + left + right + left * right)
            stack.append(i)
        
        return ans % (pow(10, 9) + 7)
      
      
    -----------------------------------------------------------------------
    
    class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)
      
 -----------------------------------------------------------------------

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        M = 10**9+7
        sums = 0
        arr.append(0) 
        stack = [-1]
        
        for i2,num in enumerate(arr):
	      #Mantain a monotone increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]   # First lesser element to the left
                left = index-stack[-1]
                right = i2-index
                sums += right*left*arr[index]
            stack.append(i2)
            
        return sums%M

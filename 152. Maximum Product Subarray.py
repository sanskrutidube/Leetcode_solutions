class Solution:
        def maxProduct(self, A):
            B = A[::-1]
            for i in range(1, len(A)):
                A[i] *= A[i - 1] or 1
                B[i] *= B[i - 1] or 1
            return max(A + B)
          
-------------------------------------------------------------

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
			
            res = max(res, curMax)
            
        return res

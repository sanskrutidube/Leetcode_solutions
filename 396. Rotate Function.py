class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        curr_sum = sum(i*nums[i] for i in range(n))
        max_sum = curr_sum

        for i in range(1, n):
            curr_sum += total_sum - n * nums[n-i]  
            max_sum = max(max_sum, curr_sum)  
            
        return max_sum
----------------------------------------------------------------

class Solution(object):
    def maxRotateFunction(self, A):
        r = curr = sum(i * j for i,j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r

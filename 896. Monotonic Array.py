class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[-1] < A[0]: 
            A = A[::-1]
        
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
-----------------------------------------------------
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)

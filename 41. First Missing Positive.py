class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        i = 1
        while i in unique:
            i += 1
        return i
------------------------------------------------------------------

class Solution:
   def firstMissingPositive(self, nums):
       nums.sort()
       res = 1
       for num in nums:
           if num == res:
               res += 1
       return res

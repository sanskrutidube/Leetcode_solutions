class Solution:
   def minimumOperations(self, nums: List[int]) -> int:
       return len({num for num in nums if num != 0})
       
----------------------------------------------------------------

class Solution:
   def minimumOperations(self, nums: List[int]) -> int:
        unique = list(set(nums) - {0})
        return len(unique)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]        
        return subsets
      
      
-----------------------------------------------------------------

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        without = self.subsets(nums[1:])
        return without + [s + [nums[0]] for s in without]

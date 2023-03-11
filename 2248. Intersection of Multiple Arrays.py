class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a=set(nums[0])
        inters=a.intersection(*nums)
        return sorted(list(inters))
------------------------------------------------------------------------
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        temp = set(nums[0])
        for i in range(1,len(nums)):
            temp = (temp & set(nums[i]))
    
        return list(sorted(temp))

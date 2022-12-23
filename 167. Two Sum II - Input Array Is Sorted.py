class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {} #collection
        for i, v in enumerate(numbers):
            if (target - v) in dic: break #find the pair present in dic.
            else: dic[v] = i+1 #Making a collection of 1st pair. 
        return sorted([dic[target - v],i+1])
            
--------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l= 0
        r= len(nums)-1
        while l<r:
            if nums[l] + nums[r] < target:
                l+=1
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                return(l+1,r+1)

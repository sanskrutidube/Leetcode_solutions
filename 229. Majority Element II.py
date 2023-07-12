class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in set(nums):
            if nums.count(i)> int(n/3):
                ans.append(i)
                
        return ans           

class Solution:
    def targetIndices(self, nums, target):
        ans = []
        for i,num in enumerate(sorted(nums)):
            if num == target: ans.append(i)
        return ans
-----------------------------------------------------

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=sorted(nums)
        le=len(n)
       
        l=[]
        for i in range(le):
            if n[i]==target:
                l.append(i)
        return l

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c1=0
        c2=0
        for i in nums:
            if i<0:
                c1+=1
            if i>0:
                c2+=1
        return(max(c1,c2))
        

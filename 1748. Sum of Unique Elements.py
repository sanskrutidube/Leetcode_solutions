class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            if nums.count(i)==1:
                sum+=i
        return sum
------------------------------------------------------------

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = []
        [uniq.append(num) for num in nums if nums.count(num) == 1]
        return sum(uniq)
        
 -------------------------------------------------------------
 
 class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for index,value in enumerate(nums):
            if count[value]==1:
                ans+=value
        return ans

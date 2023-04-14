from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd=0
        count=collections.Counter(nums)
        for k,v in count.items():
            if v%2==1:
                odd= 1
        if odd == 1:
            return False
        return True

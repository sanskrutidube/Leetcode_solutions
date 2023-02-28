class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num1=[]
        for i in nums:
            n=i*i
            num1.append(n)
        num1.sort()
        return num1

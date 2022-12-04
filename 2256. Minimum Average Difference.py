class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        sumEnd, sumFront, res, diff, n = 0, 0, 0, 1e9, len(nums)
        for num in nums:
            sumEnd += num

        for i in range(n):
            sumFront += nums[i]
            sumEnd -= nums[i]

            avg1 = sumEnd//(n-1-i) if i != n-1 else 0
            avg2 = sumFront//(i+1)

            if abs(avg1-avg2) < diff:
                diff = abs(avg1-avg2)
                res = i
        
        return res
   ---------------------------------------------------------------------------
class Solution:
    def minimumAverageDifference(self, a: List[int]) -> int:
        l=0
        r=sum(a)
        z=100001
        y=0
        n=len(a)
        
        for i in range(n-1):
            l+=a[i]
            r-=a[i]
        
            d=abs((l//(i+1))-(r//(n-i-1)))
            if d<z:
                z=d
                y=i
        
        if sum(a)//n<z:
            y=n-1
        
        return y

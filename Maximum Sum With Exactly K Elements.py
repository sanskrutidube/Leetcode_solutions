class Solution(object):
    def maximizeSum(self, nums, x):
        nums.sort()
        result=0
        while(x>0):
            maximum = max(nums)
            nums.pop()
            nums.append(maximum+1)
            result=result+maximum
            x=x-1
        return result

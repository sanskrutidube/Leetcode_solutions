class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pro=1
        for i in nums:
            pro= pro*i
        if pro>0:
            return 1
        elif pro==0:
            return 0
        else:
            return -1

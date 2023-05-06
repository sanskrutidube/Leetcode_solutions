class Solution(object):
    def findDifference(self, nums1, nums2):
        a = set(nums1) - set(nums2)
        b = set(nums2) - set(nums1)
        return [a,b]

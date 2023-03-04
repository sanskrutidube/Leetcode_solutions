class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2, nums1
        d = {}
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res = []
        for i in nums2:
            if i in d:
                res.append(i)
            else:
                continue
        return set(res)
--------------------------------------------------------------------------------------
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         return list(set(nums1) & set(nums2))
-----------------------------------------------------------------------------------------
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for i in nums1:
            if i in nums2:
                lst.append(i)
        return set(lst)

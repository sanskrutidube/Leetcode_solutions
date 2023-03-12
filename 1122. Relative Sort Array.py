class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        c = collections.Counter(arr1)
        res = []       
        for i in arr2:
            res += [i]*c.pop(i)  
        return res + sorted(c.elements())
--------------------------------------------------

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        for i in arr2:
            while i in arr1:
                a.append(i)
                arr1.remove(i)
        return(a+sorted(arr1))
        

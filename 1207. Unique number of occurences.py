from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x_Keys = Counter(arr).keys()     
        x_Values = Counter(arr).values()     
        x_Set = set(x_Values)                 
        return len(x_Keys)==len(x_Set) 
------------------------------------------------------------------------------
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    	return (lambda x: len(x) == len(set(x)))(collections.Counter(arr).values())
 
------------------------------------------------------------------------------
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        
        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        if len(set(dic.values())) != len(set(arr)):
            return False
        return True
-------------------------------------------------------------------------------
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict(Counter(arr))
        s=set(d.values())
        return len(d.values())==len(s)

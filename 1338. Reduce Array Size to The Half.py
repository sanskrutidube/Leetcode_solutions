class Solution(object):
    def minSetSize(self, arr):
        d = {}
        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
                  
        l = sorted(d.values())
        N = len(arr) // 2
        idx = 0
        
        while N > 0:
            N -= l[-idx-1]
            idx += 1
            
        return idx
        
---------------------------------------------

class Solution:
    def minSetSize(self, arr):
        count = Counter(arr)
        currentCount = 0
        currentSize = 0
        for value in sorted(count.values(), key=None, reverse=True):
            currentSize += 1
            if currentCount + value >= len(arr) // 2:
                return currentSize
            currentCount += value
                

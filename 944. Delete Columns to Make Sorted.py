class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        zipped=list(map(list,zip(*A)))
        count=0
        for item in zipped:
            if item!=sorted(item):
                count+=1
        return count
        
 --------------------------------------------------------------------
 
 class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        count = 0
        
        for i in range(n):
            for j in range(1,m):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        
        return count
	--------------------------------------------------------------------------------
  class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = []
        for i in range(len(strs)-1):
            for j in range(len(strs[0])):
                if strs[i][j] > strs[i+1][j]:
                    c.append(j)
        return len(set(c))

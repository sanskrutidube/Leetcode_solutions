class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans= [0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[j]= max(ans[j], len(str(grid[i][j])))
        return ans
        
            
        

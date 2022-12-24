class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        i,j=0,len(matrix[0]) - 1
        while i<len(matrix) and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                    i=i+1
            elif matrix[i][j]>target:
                    j=j-1
        return False
                

                    

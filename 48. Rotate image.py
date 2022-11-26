class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def reflect(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
                               
            
  ----------------------------------------------------------------------------
  
  class Solution:
    def rotate(self, A):
        A[:] = map(list, zip(*A[::-1]))
        
  -----------------------------------------------------------------------------
  
  class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
		
        n = len(matrix)
        
		# iterate through matrix
        for i in range(n):
            for j in range(i,n):
			
			    # transpose the matrix, turning rows into columns and vice versa
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			
			# reverse the resulting rows
            matrix[i].reverse()
        
----------------------------------------------------------------------------------

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
	        for j in range(i):
		        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 -------------------------------------------------------------------------------------

class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
------------------------------------------------------------------------------------

class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
                
  

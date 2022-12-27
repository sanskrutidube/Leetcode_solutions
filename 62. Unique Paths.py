class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]
        
--------------------------------------------
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP Solution
        if m == 1 or n == 1:
            return 1
        
    
        # O(m*n) Space Complexity 
        dp = [[1] * n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]      
        return dp[m-1][n-1]


--------------------------------------------
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:

		result = {}

		def All_Path(row, col):

			if row == 0 or col == 0:
				return 1

			elif (row , col ) not in result:

				result[(row , col)] = All_Path(row - 1, col) + All_Path(row, col - 1)

			return result[(row , col )]

		return All_Path(m - 1, n - 1)
Console

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen.append((c,i))
                    seen.append((j,c))
                    seen.append((i//3, c, j//3))
        return len(seen) == len(set(seen))
      
----------------------------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    
                    k = (i // 3 ) * 3 + j // 3
                
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                    
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                
                    if cur not in mMat[k]: mMat[k].add(cur)
                    else: return False
        return True
---------------------------------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        mat=[set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                cur=board[i][j]
                if cur !='.':
                    k=(i // 3) * 3 +j // 3
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                    if cur not in mat[k]: mat[k].add(cur)
                    else: return False
        return True
----------------------------------------------------------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        mat=[[set() for i in range(3)] for j in range(3)]
        
        for i in range(9):
            for j in range(9):
                cur=board[i][j]
                if cur =='.':
                    continue
                if cur in rows[i] or cur in cols[j] or cur in mat[i//3][j//3]:
                    return False
                rows[i].add(cur)
                cols[j].add(cur)
                mat[i//3][j//3].add(cur)
                    
        return True

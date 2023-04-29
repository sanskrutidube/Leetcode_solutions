class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        result=[]
        n = len(A)
        for i in range(0,n):
            tempA = A[:i+1]
            tempB = B[:i+1]
            comm = len(set(tempA)&set(tempB))
            result.append(comm)
        return result
            

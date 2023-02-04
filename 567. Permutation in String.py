class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)                   
                                                    
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  
                                                     
        for i in range(n1,n2):                      
            if ctr1 == ctr2: return True            
                                                    
            ctr2[s2[i-n1]]-= 1                      
            ctr2[s2[i   ]]+= 1

        return ctr1 == ctr2
      
 ----------------------------------------------------------------

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1
            if all([cntr[i] == 0 for i in cntr]):
                return True
        return False
        

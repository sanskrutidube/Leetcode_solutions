class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna= {}
        m=[]
        for i in range(len(s) -9):
            x=s[i:i+10]
            if x in dna:
                dna[x]=dna[x]+1
                m.append(x)
            else:
                dna[x]= 1 
        return(list(set(m)))
        
----------------------------------------------------------------------
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        res, d = [], {}
        for i in range(len(s)):
            
            if s[i:i+10] not in d: d[s[i:i+10]] = 0
            elif s[i:i+10] not in res: res.append(s[i:i+10])
                
        return res
		
		
        

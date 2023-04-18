class Solution:
    def getpower(self,num):
        count=0
        while num!=1:
            
            if num%2==0:
                num=num//2
                
            else:
                num=3*num +1
            count=count+1    
        
        return count
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l=sorted(range(lo,hi+1),key=lambda x:self.getpower(x))
        return l[k-1]
		

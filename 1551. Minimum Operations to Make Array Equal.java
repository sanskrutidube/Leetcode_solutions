class Solution {
    public int minOperations(int n) {
        return n * n / 4;
    }
}
---------------------------------------------------
  
class Solution {
    public int minOperations(int n) {
	// Take care of overflow if n is too large.
        if(n%2==1){
            n/=2;
            return (n*(n+1));
        }        
        n/=2;
        return n*n;
    }
}

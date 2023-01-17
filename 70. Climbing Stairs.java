class Solution {
    public int climbStairs(int n) {
        int dp[]=new int [n+1];
        dp[0]=1;
        dp[1]=1;
        for(int i=2;i<=n;i++) {
            dp[i]=dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}
-----------------------------------------------------
  
class Solution {
    public int climbStairs(int n) { //FIBONACCI
        if(n<=2)
            return n;
        int one =1;
        int two =2;
        for(int i = 3;i<=n;i++){
            int temp = one;
            one = two;
            two+=temp;
        }
        return two;
    }
}

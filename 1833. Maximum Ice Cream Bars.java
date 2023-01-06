class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs); // Sort costs

        for(int i=0 ;i<costs.length;++i)
            if( (coins-=costs[i])<0) // Update && check
                return i; 

        //if we still have coins after buying all the icecream :
        return costs.length;
    }
}
--------------------------------------------------------------------------------

class Solution {
    public int maxIceCream(int[] costs, int coins) {
        
        Arrays.sort(costs);
        int n = costs.length;
        int answer = 0;
        
        while (answer < n && costs[answer] <= coins) {
             
            coins -= costs[answer];
            answer += 1;
        }
        return answer;
    }
}
1833. Maximum Ice Cream Bars.java

class Solution {
    public int minimumSum(int num) {
        int nos[] = new int[4];
        for(int i=0;i<4;i++){
            nos[i]=num%10;
            num/=10;
        }
        Arrays.sort(nos);
        return Math.min(nos[0]*10 + nos[3] + nos[1]*10 + nos[2],nos[1]*10 + nos[3] + nos[0]*10 + nos[2] );
    }
}

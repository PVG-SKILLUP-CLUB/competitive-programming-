class Solution {
    public static int minimumTime(int N, int cur, int[] pos, int[] time) {
        // code here
        
        int min=Integer.MAX_VALUE;
        for(int i=0;i<N;i++)
        {
            int num=(Math.abs(cur-pos[i]))*time[i];
            min=Math.min(min,num);
        }
        
        return min;
    }
}     

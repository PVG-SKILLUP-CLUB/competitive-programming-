public class Solution {
    public int cutRod(int price[], int n) {
        int[] dp = new int[n+1];
        
        // Base case
        dp[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            int maxVal = Integer.MIN_VALUE;
            for (int j = 1; j <= i; j++) {
                maxVal = Math.max(maxVal, price[j-1] + dp[i-j]);
            }
            dp[i] = maxVal;
        }
        
        return dp[n];
    }
}

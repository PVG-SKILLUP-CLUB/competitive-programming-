 

class Solution{
    static int nCr(int n, int r)
    {
        // code here
        if(n<r) return 0;
        if(r==n || r==0) return 1;
        int dp[] = new int[n+1];
        dp[0] = 1;
        int mod = 1000000007;
        for (int i=1; i<=n; i++) {
            for (int j = Math.min(i,r); j>0; j--) {
                dp[j] = (dp[j] + dp[j-1]) % mod;
            }
        }
        return dp[r];
    }
}

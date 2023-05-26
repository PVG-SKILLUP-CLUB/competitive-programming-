class Solution {
	static int helper(int[][] dp, int n, int i, int x) {
		if (Math.pow(i, x) > n)
			return 0;
		if (Math.pow(i, x) == n)
			return 1;
		if (dp[i][n] != -1)
			return dp[i][n];
		int pick = helper(dp, n - (int) Math.pow(i, x), i + 1, x);
		int notPick = helper(dp, n, i + 1, x);
		return dp[i][n] = (pick % 1000000007 + notPick % 1000000007) % 1000000007;
	}

	static int numOfWays(int n, int x) {
		// code here
		int[][] dp = new int[n + 1][n + 1];
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++)
				dp[i][j] = -1;
		}
		return helper(dp, n, 1, x);
	}
}

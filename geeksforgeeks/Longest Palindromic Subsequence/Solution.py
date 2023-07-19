class Solution:
    def longestPalinSubseq(self, S):
        n = len(S)
        # Initialize a 2D matrix of size n x n to store lengths of palindromic subsequences
        dp = [[0] * n for _ in range(n)]
        
        # All single characters are palindromic subsequences of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the matrix diagonally, considering substrings of different lengths
        for cl in range(2, n+1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if S[i] == S[j] and cl == 2:
                    dp[i][j] = 2
                elif S[i] == S[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        # Return the length of the longest palindromic subsequence of the entire string
        return dp[0][n-1]

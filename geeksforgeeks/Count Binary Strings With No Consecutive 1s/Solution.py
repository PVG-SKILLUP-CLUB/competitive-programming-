class Solution: 
    def mult(self, A, B, MOD):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j])%MOD
        return C
        
    def power(self, A, n, MOD):
        if n == 1:
            return A
        H = self.power(A, n//2, MOD)
        res = self.mult(H, H, MOD)
        if n%2:
            res = self.mult(res, A, MOD)
        return res
        
    def countStrings(self, N): 
        MOD = 10**9 + 7
        return self.power([[1, 1], [1, 0]], N+1, MOD)[0][0]

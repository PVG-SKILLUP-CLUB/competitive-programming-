class Solution:
    def maxPossibleValue(self, N, A, B): 
        for i in range(N):
            B[i] = (B[i]//2)*2
            
        res = sum(l*c for l, c in zip(A, B))
        if sum(B)%4:
            res -= min(2*l for l, c in zip(A, B) if c > 0)
        
        return res

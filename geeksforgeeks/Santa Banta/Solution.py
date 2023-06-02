
from collections import deque
class Solution:
    def precompute(self):
        N = 2*10**6
        is_prime = [True]*N
        is_prime[0] = is_prime[1] = False

        for i in range(2, N):
            if is_prime[i]:
                for j in range(i*i, N, i):
                    is_prime[j] = False
        
        self.primes = [i for i in range(N) if is_prime[i]]
        
    
    def helpSanta(self, n, m, g):
        if m == 0:
            return -1 
        visited = [False]*(n+1)
        def bfs(u):
            Q = deque([u])
            res = 0
            visited[u] = True
            while Q:
                u = Q.popleft()
                res += 1
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        Q.append(v)
            return res
        
        k = max(bfs(u) for u in range(1, n+1) if not visited[u])
        return self.primes[k-1]
       

from typing import List


from typing import List
from collections import Counter
class Fenwick:
    def __init__(self, n):
        self.T = [[0]*26 for _ in range(n)]
        self.n = n
        self.F = lambda x: x&(x+1)
        self.H = lambda x: x|(x+1)
    
    def update(self, ind, c, delta):
        c = ord(c) - ord('a')
        while ind < self.n:
            self.T[ind][c] += delta
            ind = self.H(ind)
    
    def query(self, ind):
        result = [0]*26
        while ind >= 0:
            for c in range(26):
                result[c] += self.T[ind][c]
            ind = self.F(ind) - 1
        return result
    
    def range_query(self, left, right):
        return [r- l for r, l in zip(self.query(right), self.query(left-1))]
       
class Solution:
    def easyTask(self,n,s,q,queries) -> List[int]:
        tree = Fenwick(n)
        s = list(s)
        for ind, c in enumerate(s):
            tree.update(ind, c, 1)
        
        res = []
        for query in queries:
            if query[0] == '1':
                ind, char = int(query[1]), query[2]
                tree.update(ind, s[ind], -1)
                s[ind] = char
                tree.update(ind, s[ind], 1)
            else:
                left, right, k = int(query[1]), int(query[2]), int(query[3])
                counter = tree.range_query(left, right)
       
                for c in range(25, -1, -1):
                    if k > counter[c]:
                        k -= counter[c]
                    else:
                        res.append(chr(c + ord('a')))
                        break
        return res

from typing import List

class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        discrete = dict()
        for s, e in intervals:
            discrete[s] = discrete.get(s, 0) + 1
            discrete[e] = discrete.get(e, 0)
            discrete[e+1] =  discrete.get(e+1, 0) - 1
        
        res, cur = -1, 0
        for t in sorted(discrete):
            cur += discrete[t]
            if cur >= k:
                res = t
        return res


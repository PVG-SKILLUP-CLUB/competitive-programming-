from bisect import bisect_left
class Solution:
    def secondSmallest(self, S, D):
        if S ==1 or D ==1 or S >= 9*D:
            return "-1"
            
        o = int(9*(D-1) + 1 >= S)
        n, d = (S-o)//9, (S-o)%9
        m = int(d >= 1)
        z = D - n - o - m
            
        res = [1]*o + [0]*z + [d]*m + [9]*n
        
        j = min(bisect_left(res, 9), D - 1)
        res[j] -= 1
        res[j-1] += 1
        
        return ''.join(map(str, res))

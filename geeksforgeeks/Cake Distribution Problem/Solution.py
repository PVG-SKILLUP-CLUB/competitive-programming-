class Solution():
    def maxSweetness(self, sw, n, k):
        l = 1
        r = 10**9
        ans = 0
        while l <= r:
            m = (l+r)//2
            p = 0
            cur = 0
            for i in range(0,n):
                cur += sw[i]
                if cur >= m:
                    p += 1
                    cur = 0
            if p >= k+1:
                ans = m
                l = m+1
            else:
                r = m-1
        return ans

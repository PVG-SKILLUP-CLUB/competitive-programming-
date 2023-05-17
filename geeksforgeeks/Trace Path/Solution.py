class Solution:
    def isPossible(self, n, m, s):
        minx, maxx, miny, maxy = 0, 0, 0, 0
        dx, dy = 0, 0
        for d in s:
            if d == 'L':
                dx -= 1
            if d == 'R':
                dx += 1
            if d == 'U':
                dy += 1
            if d == 'D':
                dy -= 1
            minx = min(minx, dx)
            maxx = max(maxx, dx)
            miny = min(miny, dy)
            maxy = max(maxy, dy)
        return int(maxx-minx < m and maxy-miny < n)

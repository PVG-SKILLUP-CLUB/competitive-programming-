class Solution:
    def minimumNumber(self, n, arr):
        m=z=min(arr)
        for i in arr:
            if i%z<m and i%z!=0:
                m=i%z
        return m

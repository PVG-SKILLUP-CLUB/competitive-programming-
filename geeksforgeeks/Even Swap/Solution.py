class Solution():
    def lexicographicallyLargest(self, a, n):
        start = 0
        end = 1
        while start<n and end<n:
            if (a[start]+a[end]) % 2 == 0:
                end +=1
            else:
                a[start:end] = sorted(a[start:end],reverse= True)
                start = end
                end +=1
        if end == n:
            a[start:end] = sorted(a[start:end],reverse= True)
        return a

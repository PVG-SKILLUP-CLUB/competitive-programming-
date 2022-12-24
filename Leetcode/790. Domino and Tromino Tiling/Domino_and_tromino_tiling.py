class Solution:

    def numTilings(self, n: int) -> int:

        ls=[0,1,2,5]

        mod=10**9+7

        if n<=3:

            return ls[n]

        for i in range(4,n+1):

            ans=2*ls[i-1]+ls[i-3]

            ans%=mod

            ls.append(ans)

        return ls[n]

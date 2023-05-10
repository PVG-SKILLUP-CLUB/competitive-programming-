from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        left=[A[0]]
        for i in range(1,N):
            left.append(max(A[i],left[-1]))
        right=[A[-1]]
        for i in range(N-2,-1,-1):
            right.append(min(A[i],right[-1]))
        right=right[::-1]
        ans=0
        for i in range(1,N):
            if left[i-1]+right[i]>=K:
                ans+=1
        return ans

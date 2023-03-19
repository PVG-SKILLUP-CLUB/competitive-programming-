from typing import List


class Solution:
      def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
       
        left, right = [0]*N, [0]*N
        lc, rc = set(), set()
        for i in range(N):
            lc.add(A[i])
            left[i] = len(lc)
            rc.add(A[N-1-i])
            right[N-1-i] = len(rc)
        
        ans = []
        for i in range(N):
            lc = 0 if i-1 < 0 else left[i-1]
            rc = 0 if i+1 >= N else right[i+1]
            ans.append(lc-rc)
        return ans

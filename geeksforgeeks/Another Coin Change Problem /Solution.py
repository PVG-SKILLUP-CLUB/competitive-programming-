from typing import List


class Solution:
    def makeChanges(self, N : int, K : int, target : int, coins : List[int]) -> bool:
        # code here
        coins.sort()
        prev, cur = set(coins), set()
        for times in range(1, K):
            cur.clear()
            for v in prev:
                for c in coins:
                    if v + c > target: break
                    cur.add(v+c)
            prev, cur = cur, prev
        return target in prev

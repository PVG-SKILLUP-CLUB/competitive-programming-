from typing import List

from collections import Counter
class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        C=Counter(arr)
        f_v=set(C.values())
        if len(C)==len(f_v):
            return True
        else:
            return False

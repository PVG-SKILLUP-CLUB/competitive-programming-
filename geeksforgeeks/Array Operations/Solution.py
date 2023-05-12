from typing import List
class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        ans = 0
        prev_num = 0
        num_zero=0
        for i in arr:
            if i:       # i  != 0
                if not prev_num:    # prev_num == 0
                    num_zero += 1
            prev_num = i
        return num_zero

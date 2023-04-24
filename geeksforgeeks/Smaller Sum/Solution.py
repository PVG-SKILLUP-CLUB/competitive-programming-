from typing import List


class Solution:
    def smallerSum(self, n : int, a : List[int]) -> List[int]:
        arr = a.copy()
        arr.sort()
        dic = {arr[0]:0}
        total = 0
        
        for i in range(1,n):
            total += arr[i-1]     


            if arr[i] not in dic:
                dic[arr[i]] = total

 

        ans = []

        for elm in a:
            ans.append(dic[elm])
            
        return ans

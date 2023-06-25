
from typing import List


class Solution:
    def MinCost(self, n : int, prices : List[int], dislike : List[int]) -> int:
        # code here
        if(len(set(dislike)) == 1):
            return -1
        else:
            tl=[]
            for i in range(n):
                tl.append([prices[i],dislike[i]])
            tl=sorted(tl)
            tp=1
            x=tl[0]
            while(tp<len(tl)):
                y=tl[tp]
                if(x[1] != y[1]):
                    return x[0]+y[0]
                tp+=1



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(100000)
        
        
        dislike=IntArray().Input(100000)
        
        obj = Solution()
        res = obj.MinCost(n, prices, dislike)
        
        print(res)
        

# } Driver Code Ends

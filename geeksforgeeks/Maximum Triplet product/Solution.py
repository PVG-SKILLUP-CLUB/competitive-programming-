#User function Template for python3

from heapq import nlargest, nsmallest

class Solution:

    def maxTripletProduct (self, arr,  n): 

        #Complete the function

        l1, l2, l3 = nlargest(3, arr) 

        s1, s2 = nsmallest(2, arr)

        return max(l1*l2*l3, s1*s2*l1)

#{ 

 # Driver Code Starts

#Initial Template for Python 3



import sys



for _ in range(0,int(input())):

    

    n = int(input())

    arr = list(map(int,input().strip().split()))

    ob=Solution()

    res = ob.maxTripletProduct(arr, n)

    print(res)

# } Driver Code Ends

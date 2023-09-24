from collections import Counter

class Solution:

    def duplicates(self, arr, n): 

    	# code here

    	x=Counter(arr)

    	res=[]

    	for i in x:

    	    if x[i]>1:

    	        res.append(i)

    	res.sort()

    	return res if len(res)>0 else [-1]

#{ 

 # Driver Code Starts

if(__name__=='__main__'):

    t = int(input())

    for i in range(t):

        n = int(input())

        arr = list(map(int, input().strip().split()))

        res = Solution().duplicates(arr, n)

        for i in res:

            print(i,end=" ")

        print()







# } Driver Code Ends

#User function Template for python3



class Solution():

    def no_of_subarrays(self, n,arr):

        #your code goes here

        ans=zeros=0 

        for i in arr:

            if i==0: 

                zeros+=1

                ans+=zeros 

            else: 

                zeros=0 

        return ans; 





#{ 

 # Driver Code Starts

#Initial Template for Python 3





for _ in range(int(input())):

    n = int(input())

    arr = [int(i) for i in input().split()]

    print(Solution().no_of_subarrays(n, arr))

# } Driver Code Ends

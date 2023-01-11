#User function Template for python3



class Solution:

    def minIncrements(self, arr, N): 

        # Code here

        arr.sort()

        res=0

        for i in range(N-1):

            while arr[i+1]==arr[i] or arr[i+1]<arr[i]:

                arr[i+1]+=1

                res+=1

        return res







#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

    

    T = int(input())

    while T > 0: 

        N=int(input())

        arr = [int(i) for i in input().split()]

        ob = Solution()

        print(ob.minIncrements(arr,N))

        

        T -= 1

# } Driver Code Ends

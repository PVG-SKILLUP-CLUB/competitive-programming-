#User function Template for python3

class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        for i in range(2,n+1):
            if n%i==0:
                return False
            n-=n//i
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends

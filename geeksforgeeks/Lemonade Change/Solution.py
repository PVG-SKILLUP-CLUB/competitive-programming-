#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):

        cash5,cash10,=0,0
        cash20=0
        for i in bills:
            if i==5:
                cash5+=1
            elif i==10:
                if cash5>=1:
                    cash5-=1
                    cash10+=1
                else:
                    return False
            
            elif i==20:
                if cash10>=1 and cash5 >=1:
                    cash10-=1
                    cash5-=1
                    cash20+=1
                elif cash5>=3:
                    cash5-=3
                    cash20+=1
                else:
                    return False

        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends

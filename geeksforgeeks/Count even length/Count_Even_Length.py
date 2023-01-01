#User function Template for python3

import math

class Solution:

    def nCr(self, n, r):

        f = math.factorial

        return f(n) // f(r) // f(n-r)

    def compute_value(self, n):

        return self.nCr(2*n, n)%1000000007





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

	T=int(input())
	for i in range(T):

		n = int(input())

		ob = Solution()

		ans = ob.compute_value(n)

		print(ans)

# } Driver Code Ends

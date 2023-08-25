#User function Template for python3

class Solution:

	def isPalindrome(self, S):

		# code hereS

		S1=""

		for i in range(1,len(S)+1):

		    S1+=S[-1*i]

		return 1 if S==S1 else 0





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__':

	T=int(input())

	for i in range(T):

		S = input()

		ob = Solution()

		answer = ob.isPalindrome(S)

		print(answer)



# } Driver Code Ends

#User function Template for python3



class Solution:

    ##Complete this function

    # Function to check if given number n is a power of two.

    def isPowerofTwo(self,n):

        ##Your code here

        ans=0

        i=0

        while i<n:

            if 2**i==n:

                return True

            elif 2**i>n:

                return False

            i+=1



#{ 

 # Driver Code Starts

#Initial Template for Python 3



import math





def main():

    

    T=int(input())

    

    while(T>0):

        

        

        n=int(input())

        ob=Solution()

        if ob.isPowerofTwo(n):

            print("YES")

        else:

            print("NO")

        

        T-=1



if __name__=="__main__":

    main()

# } Driver Code Ends

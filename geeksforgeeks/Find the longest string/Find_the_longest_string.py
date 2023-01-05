#User function Template for python3


class Solution():

    def longestString(self, arr, n):

        #your code goes here

        arr.sort()

        m=""

        s=set()

        for i in arr:

            k=len(i)

            t=""

            f=0

            for p in range (k-1):

                t+=i[p]

                if t not in s:

                    f=1

                    break

            s.add(i)

            if f==0:

                if len(i)>len(m):

                    m=i

        return m




#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == "__main__":

    for _ in range(int(input())):

        n = int(input())

        arr = [i for i in input().split()]

        print(Solution().longestString(arr,n))

# } Driver Code Ends

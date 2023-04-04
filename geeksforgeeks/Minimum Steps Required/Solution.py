class Solution:

    def minSteps(self, s : str) -> int:

        # code here

        i=0;ans=0

        while i<len(s) and s[i]==s[0]:

            i+=1

        if i==len(s):

            return ans+1 

        t=s[i]

        while i<len(s): 

            if s[i]==t: 

                while i<len(s) and s[i]==t:

                    i+=1

                if i==len(s): 

                    return ans+2 

                else:

                    ans+=1 

                    while i<len(s) and s[i]==s[0]:

                        i+=1

        return ans+1

        







#{ 

 # Driver Code Starts

if __name__=="__main__":

    t = int(input())

    for _ in range(t):

        

        str = (input())

        

        obj = Solution()

        res = obj.minSteps(str)

        

        print(res)

        



# } Driver Code Ends

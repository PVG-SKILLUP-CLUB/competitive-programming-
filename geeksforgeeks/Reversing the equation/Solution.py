class Solution:
    def reverseEqn(self, s):
        stack=""
        ans=[]
        for i in range(len(s)):
            if not s[i].isdigit():
                ans.append(stack)
                ans.append(s[i])
                stack=""
            else:
                stack+=(s[i])
        ans.append(stack)
        ans=ans[::-1]
        return"".join(ans)

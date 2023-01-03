class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:

        res=0

        for i in range(len(strs[0])):

            a=strs[0][i]

            for j in range(1,len(strs)):

                if a<= strs[j][i]:

                    a=strs[j][i]

                else:

                    res+=1

                    break

        return res

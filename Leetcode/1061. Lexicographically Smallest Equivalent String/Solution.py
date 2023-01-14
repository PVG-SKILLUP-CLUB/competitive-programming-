class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        dict={}

        res=[]

        

        def find(x):

            dict.setdefault(x,x)  

            if x!=dict[x]:

                dict[x]=find(dict[x])

            return dict[x]

        

        def union(x,y):

            rootx=find(x)

            rooty=find(y)

            if rootx>rooty:

                dict[rootx]=rooty

            else:

                dict[rooty]=rootx

        for i in range(len(s1)):

            union(s1[i],s2[i])

        

        for c in baseStr:

            res.append(find(c))

        

        return ''.join(res)

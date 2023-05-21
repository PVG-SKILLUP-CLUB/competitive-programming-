class Solution:
    def findMoves(self,n,chairs,passengers):
        #code here
        sumi=0
        chairs.sort()
        passengers.sort()
        for i,j in zip(chairs,passengers):
            sumi+=abs(i-j)
        return sumi

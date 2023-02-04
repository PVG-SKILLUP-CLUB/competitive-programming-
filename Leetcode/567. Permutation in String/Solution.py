class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        ln = len(s1)

        mp1 = collections.Counter(s1) 

        for i in range(len(s2) - ln + 1):

            sb = s2[i:i+ln] 

            if mp1 == collections.Counter(sb):

                return True

        return False

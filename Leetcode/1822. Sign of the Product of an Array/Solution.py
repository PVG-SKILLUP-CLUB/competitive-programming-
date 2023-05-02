class Solution:

    def arraySign(self, nums: List[int]) -> int:

        sign=0

        prod=1

        for n in nums:

            prod*=n

        if prod<0:

            sign=-1

        elif prod>0:

            sign=1

        return sign

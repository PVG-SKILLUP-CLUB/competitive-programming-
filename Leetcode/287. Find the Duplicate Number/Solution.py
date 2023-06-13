class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        num=set()

        for n in nums:

            if n in num:

                return n

            num.add(n)

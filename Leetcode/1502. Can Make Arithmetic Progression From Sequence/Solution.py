class Solution:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        diff=arr[0]-arr[1]

        for i in range(2,len(arr)):

            if diff!=arr[i-1]-arr[i]:

                return 0

        return 1

class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans=[]

        for i in range(0,n):

            ans.append(nums[i])

            ans.append(nums[n+i])       

        return ans

class Solution:
    def solve(self, ans, nums, i):
        if i == len(nums):
            if "".join(nums[:]) not in ans:
                ans.append("".join(nums[:]))
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.solve(ans, nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]
    
    def find_permutation(self, S):
        ans = []
        nums=list(S)
        self.solve(ans, nums, 0)
        ans=sorted(ans)
        return ans

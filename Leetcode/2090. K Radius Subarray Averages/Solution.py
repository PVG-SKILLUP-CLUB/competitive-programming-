class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = [-1] * len(nums)
        
        if k == 0:
            return nums

        n = len(nums)
        
        if 2 * k + 1 > n:
            return averages

        window_sum = sum(nums[:2 * k + 1])
        averages[k] = window_sum // (2 * k + 1)

        for i in range(2 * k + 1, n):
            
            window_sum = window_sum - nums[i - (2 * k + 1)] + nums[i]
            averages[i - k] = window_sum // (2 * k + 1)

        return averages

class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []     

        i = 0 

        

        while i < len(nums): 

            start = nums[i]  

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 

                i += 1 

            

            if start != nums[i]: 

                ranges.append(str(start) + "->" + str(nums[i]))

            else: 

                ranges.append(str(nums[i]))

            

            i += 1

        return ranges

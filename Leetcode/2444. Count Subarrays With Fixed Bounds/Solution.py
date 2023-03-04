class Solution:

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        # min_position, max_position: the MOST RECENT positions of minK and maxK.

        # left_bound: the MOST RECENT value outside the range [minK, maxK].

        answer = 0

        min_position = max_position = left_bound = -1

        

        # Iterate over nums, for each number at index i:

        for i, number in enumerate(nums):

            # If the number is outside the range [minK, maxK], update the most recent left_bound.

            if number < minK or number > maxK:

                left_bound = i

                

            # If the number is minK or maxK, update the most recent position.

            if number == minK:

                min_position = i

            if number == maxK:

                max_position = i

                

            # The number of valid subarrays equals the number of elements between left_bound and 

            # the smaller of the two most recent positions.

            answer += max(0, min(min_position, max_position) - left_bound)

            

        return answer

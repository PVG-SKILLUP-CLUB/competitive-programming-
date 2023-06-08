#Brute force solution
class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:

        cnt=0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j]<0:

                    cnt+=1

        return cnt

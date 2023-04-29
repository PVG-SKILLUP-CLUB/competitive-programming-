class Solution:
    def findNumber(self, N : int) -> int:
        soln, prod = 0, 5
        digit = 1
        while (N - prod > 0):
            N -= prod
            prod *= 5
            digit += 1
        for i in range(1, digit + 1):
            for j in range(1, 10, 2):
                temp = 5 ** (digit - i)
                if temp == 0:
                    soln = soln * 10 + (2 * N) - 1
                    break
                if N - temp > 0:
                    N -= temp
                else:
                    soln = soln * 10 + j
                    break
        return soln

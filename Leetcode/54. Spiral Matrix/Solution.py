class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        while matrix and matrix[0]:

                res += matrix.pop(0) + [i.pop(-1) for i in matrix]

                

                if matrix and matrix[0]:

                    res += matrix.pop(-1)[::-1] + list(reversed([i.pop(0) for i in matrix]))

                    

        return res

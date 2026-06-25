class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_i = set()
        set_j = set()
        for i in range (m):
            for j in range (n):
                if (matrix[i][j] == 0):
                    set_i.add(i)
                    set_j.add(j)
        for i in range (m):
            for j in range(n):
                if i in set_i or j in set_j:
                    matrix[i][j] = 0

        

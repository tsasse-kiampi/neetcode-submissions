class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            matrix[i] = [0]*m

        for row in matrix:
            for j in cols:
                row[j] = 0

                          
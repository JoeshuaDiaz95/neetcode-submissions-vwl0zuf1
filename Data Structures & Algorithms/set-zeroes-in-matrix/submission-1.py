class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        coverted = set()


        for r in range(rows):
            for c in range(cols):
                if (r,c) in coverted:
                    continue
                if matrix[r][c] == 0:
                    for i in range (cols):
                        if matrix[r][i] == 0:
                            continue
                        matrix[r][i] = 0
                        coverted.add((r,i))
                    for j in range (rows):
                        if matrix[j][c] == 0:
                            continue
                        matrix[j][c] = 0
                        coverted.add((j,c))
        
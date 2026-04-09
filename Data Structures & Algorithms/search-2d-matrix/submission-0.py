class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows=len(matrix)
        cols=len(matrix[0])

        #binary search for rows
        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid_col = (top + bottom) // 2

            if target > matrix[mid_col][-1]:
                top = mid_col + 1
            elif target < matrix[mid_col][0]:
                bottom = mid_col - 1
            else: 
                break

        if not top <= bottom:
            return False

        p_row = (top + bottom) // 2

        #binary search for col
        left = 0 
        right = cols - 1

        while left <= right:
            mid_col = (left + right) // 2

            if target == matrix[p_row][mid_col]:
                return True
            elif target > matrix[p_row][mid_col]:
                left = mid_col + 1
            elif target < matrix[p_row][mid_col]:
                right = mid_col - 1
        return False
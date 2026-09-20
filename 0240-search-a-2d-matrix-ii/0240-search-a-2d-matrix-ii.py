class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        cols = len(matrix[0])-1
        row = rows
        col = 0
        while row >= 0 and col <= cols:
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                row -= 1
            else:
                col += 1
        return False
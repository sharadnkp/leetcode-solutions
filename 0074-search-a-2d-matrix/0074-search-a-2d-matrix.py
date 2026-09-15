class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0])-1
        while low <= high:
            guess = (low+high)//2
            row = guess//len(matrix[0])
            col = guess%len(matrix[0])
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                high = guess-1
            else:
                low = guess+1
        return False
class Solution:
    def countVal(self, matrix, n , m , guess):
        row = n-1
        col = 0
        count = 0
        while row >= 0 and col < m:
            if matrix[row][col] <= guess:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        rows = len(matrix)
        cols = len(matrix[0])
        while low < high:
            guess = (low+high)//2
            count = self.countVal(matrix, rows, cols, guess)
            if count < k:
                low = guess+1
            else:
                high = guess
        return low
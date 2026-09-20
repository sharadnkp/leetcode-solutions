class Solution:
    def countVal(self, m, n, guess):
        count = 0
        for i in range(1, m + 1):
            count += min(guess // i, n)
        return count


    def findKthNumber(self, m, n, k):
        low = 1
        high = m * n

        while low < high:
            guess = (low + high) // 2

            count = self.countVal(m, n, guess)

            if count < k:
                low = guess + 1
            else:
                high = guess

        return low

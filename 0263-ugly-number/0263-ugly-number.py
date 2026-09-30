class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        factors = [2,3,5]
        for i in factors:
            while True:
                if n%i == 0:
                    n //= i
                else:
                    break
        return n == 1
                
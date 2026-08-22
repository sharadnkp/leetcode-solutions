class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = n
        sum_n = 0
        product_n = 1
        while n>0:
            digit = n%10
            sum_n += digit
            product_n *= digit
            n //= 10
        return a%(sum_n+product_n) == 0
            
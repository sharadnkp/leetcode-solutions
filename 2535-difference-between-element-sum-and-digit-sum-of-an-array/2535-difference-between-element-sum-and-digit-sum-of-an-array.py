class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for i in nums:
            element_sum += i
            while i>0:
                digit = i%10
                digit_sum += digit
                i//=10
        return abs(element_sum - digit_sum)
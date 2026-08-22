class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_length = 0
        for num in nums:
            if num == 1:
                current += 1
                max_length = max(current, max_length)
            else:
                current = 0
        return max_length
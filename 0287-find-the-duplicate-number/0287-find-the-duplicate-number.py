class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d = [False]*(len(nums)+1)
        for i in nums:
            if d[i]:
                return i
            d[i] = True
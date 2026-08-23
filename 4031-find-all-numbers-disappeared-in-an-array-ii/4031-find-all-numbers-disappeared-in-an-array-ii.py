class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        seen = set(nums)
        zelvoranki = nums
        ans = []
        i = lower
        while i <= upper:
            if i in seen:
                i += 1
                continue
            start = i
            while i <= upper and i not in seen:
                i += 1
            ans.append([start, i - 1])
        return ans
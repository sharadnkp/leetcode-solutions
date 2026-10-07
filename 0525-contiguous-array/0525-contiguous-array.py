class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        ans = 0
        prefix = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

            prefix += nums[i]

            if prefix in d:
                ans = max(ans, i - d[prefix])
            else:
                d[prefix] = i
        return ans

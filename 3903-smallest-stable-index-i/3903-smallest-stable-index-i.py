class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_ans = [0]*len(nums)
        min_ans[len(nums)-1] = nums[len(nums)-1]
        max_ans = [0]*len(nums)
        max_ans[0] = nums[0]
        for i in range(1,len(nums)):
            max_ans[i] = max(nums[i],max_ans[i-1])

        for i in range(len(nums)-2,-1,-1):
            min_ans[i] = min(nums[i],min_ans[i+1])

        for i in range(len(nums)):
            if (max_ans[i]-min_ans[i])<=k:
                return i
        return -1



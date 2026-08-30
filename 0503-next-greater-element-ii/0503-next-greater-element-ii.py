class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1]*len(nums)
        for i in range(2*len(nums)):
            while stack and nums[i%len(nums)] > nums[stack[-1]]:
                prev = stack.pop()
                answer[prev] = nums[i%len(nums)]
            stack.append(i%len(nums))
        return answer
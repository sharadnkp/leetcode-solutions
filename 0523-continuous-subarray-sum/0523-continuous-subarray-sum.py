class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum % k in remainder_map:
                if i - remainder_map[prefix_sum%k] >= 2:
                    return True
            else:
                remainder_map[prefix_sum%k] = i
        return False
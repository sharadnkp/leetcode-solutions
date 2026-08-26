class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0:1}
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - goal
            if needed in prefix_map:
                count += prefix_map[needed]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0)+1
        return count
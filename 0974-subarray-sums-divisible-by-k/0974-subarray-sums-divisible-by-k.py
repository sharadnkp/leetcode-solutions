class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum % k in remainder_map:
                count += remainder_map[prefix_sum % k]
            remainder_map[prefix_sum%k] = remainder_map.get(prefix_sum%k,0)+1
        return count
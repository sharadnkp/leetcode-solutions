class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        prefix_count = {0:1}
        for num in nums:
            prefix += num
            needed = prefix - k
            if needed in prefix_count:
                count += prefix_count[needed]
            prefix_count[prefix] = prefix_count.get(prefix, 0)+1

        return count
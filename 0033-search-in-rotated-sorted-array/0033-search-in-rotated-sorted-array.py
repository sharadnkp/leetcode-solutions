class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        last = nums[-1]

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] == target:
                return guess

            # target and nums[guess] are in the right sorted part
            elif target > last and nums[guess] > last:
                if target < nums[guess]:
                    high = guess - 1
                else:
                    low = guess + 1

            # target is in the left sorted part
            elif target <= last and nums[guess] <= last:
                if target < nums[guess]:
                    high = guess - 1
                else:
                    low = guess + 1

            # target is in left part, mid is in right part
            elif target > last and nums[guess] <= last:
                high = guess - 1

            # target is in right part, mid is in left part
            else:
                low = guess + 1

        return -1
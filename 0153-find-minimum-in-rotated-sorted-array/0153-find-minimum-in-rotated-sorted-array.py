class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>nums[len(nums)-1]:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return nums[ans]
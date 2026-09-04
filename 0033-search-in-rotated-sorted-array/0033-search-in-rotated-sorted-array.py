class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        low = 0
        high = ans-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1

        low = ans
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1
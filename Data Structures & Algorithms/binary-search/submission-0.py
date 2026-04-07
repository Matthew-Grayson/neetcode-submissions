import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use binary search algorithm to find target in nums
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1    



        # index = bisect.bisect_left(nums, target)
        # if nums[index] == target and index < len(nums):
        #     return index
        # return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search index of min value in list
        # perform comparison 
        # use first or last value in nums to deternine half to eliminate
        # which half to eliminate from search

        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        print("pivot: ", pivot, "value: ", nums[pivot])

        if target >= nums[pivot]: 
            if target <= nums[len(nums) - 1]:
                left = pivot
                right = len(nums) - 1
            else:
                left = 0
                right = pivot
        else:
            return -1

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1 
            else:
                return mid
        return -1
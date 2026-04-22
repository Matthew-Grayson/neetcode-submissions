class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        print("pivot: ", pivot, "value: ", nums[pivot])

        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1 
            else:
                return mid
        return -1
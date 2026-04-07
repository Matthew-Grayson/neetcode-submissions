class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # compare mid value with target to bisect list
        # continue search in upper or lower half based on comparison
        # continue bisecting until target found or all bisections checked

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return  -1
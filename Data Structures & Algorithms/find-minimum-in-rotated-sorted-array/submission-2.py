class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # track min val inialized as math.inf or nums[0]
        # for each iteration compare nums[right] and nums[left] to determine 
        out = math.inf
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            out = min(out, nums[mid])
            if nums[left] > nums[mid] or nums[left] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        
        return out

    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        left = 0
        last_index = len(nums) - 1
        res = []

        while left < last_index - 1:
            if nums[left] > 0:
                break
            mid = left + 1
            right = last_index
            target = 0 - nums[left]
            while mid < right:
                if nums[mid] + nums[right] < target:
                    mid += 1
                elif nums[mid] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[mid], nums[right]])
                    temp = mid
                    right -= 1
                    while mid < right and nums[temp] == nums[mid]:
                        mid += 1
            temp = left
            while left < last_index - 1 and nums[left] == nums[temp]:
                left += 1
        return res
                        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, nums[0]
        left, right = 0, 0
        while right < len(nums):
            curSum += nums[right]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
                left = right + 1
                right = left
            else:
                right += 1
        return maxSum
            
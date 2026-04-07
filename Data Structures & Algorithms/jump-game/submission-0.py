class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start, goal = 0, len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= goal - i:
                goal = i
        return goal == 0
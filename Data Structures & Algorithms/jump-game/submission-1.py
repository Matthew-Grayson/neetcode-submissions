class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumplist = []
        jumplist.append(len(nums) - 1)

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= min(jumplist):
                jumplist.append(i)

        return 0 in jumplist
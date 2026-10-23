class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.calcRob(nums[1:]), self.calcRob(nums[:-1]))       


    def calcRob(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = rob2
            rob2 = max(rob2, num + rob1)
            rob1 = temp

        return rob2
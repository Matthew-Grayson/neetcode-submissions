class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        for i, x in enumerate(nums):
            ans[i] = x
            ans[i + len(nums)] = x
        return ans
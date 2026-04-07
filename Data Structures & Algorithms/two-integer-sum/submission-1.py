class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i, x in enumerate(nums):
            diff = target - x
            if diff in numsDict:
                return [numsDict[diff], i]
            numsDict[x] = i

        return -1
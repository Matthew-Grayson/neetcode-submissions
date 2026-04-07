class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = []
        for x in nums:
            if x in uniqueNums:
                return True
            uniqueNums.append(x)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for x in nums:
            if x in uniqueNums:
                return True
            uniqueNums.add(x)
        return False

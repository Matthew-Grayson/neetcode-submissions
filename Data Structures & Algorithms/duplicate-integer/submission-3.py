class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for x in nums:
            if x in uniqueSet:
                return True
            uniqueSet.add(x)
        return False
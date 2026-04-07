class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visitedNums = set()
        for num in nums:
            if num in visitedNums:
                return True
            visitedNums.add(num)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check each value once
        visited = set()

        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False
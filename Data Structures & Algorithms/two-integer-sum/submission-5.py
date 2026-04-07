class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], i]
            visited[num] = i
        return
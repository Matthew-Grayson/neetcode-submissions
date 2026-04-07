class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through nums; store each value in hash set
        # for each element, check hash set for complement that adds up to target
        visited = {}

        for idx, num in enumerate(nums):
            diff =  target - num
            if diff in visited:
                return [visited[diff], idx]
            visited[num] = idx

        return
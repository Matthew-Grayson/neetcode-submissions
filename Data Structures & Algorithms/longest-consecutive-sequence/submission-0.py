class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for x in nums:
            length = 1
            if x - 1 in numSet:
                continue
            while x + length in numSet:
                length += 1
            longest = max(longest, length)
        return longest

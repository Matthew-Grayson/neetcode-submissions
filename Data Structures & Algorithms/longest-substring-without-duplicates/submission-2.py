class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substring = set()
        length = 0
        while right < len(s):
            while s[right] and s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            length = max(length, right - left + 1)
            right += 1

        return length


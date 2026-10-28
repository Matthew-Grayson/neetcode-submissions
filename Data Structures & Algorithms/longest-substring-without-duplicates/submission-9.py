class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left, right = 0, 0
        substr = set()

        while right < len(s):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[right])
            length = max(length, right - left + 1)
            right += 1

        return length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left, right = 0, 0
        substr = set()
        res = 0
        while right < len(s):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res
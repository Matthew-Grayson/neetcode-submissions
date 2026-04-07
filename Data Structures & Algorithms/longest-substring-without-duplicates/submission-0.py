class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left, right = 0, 1
        substr = [s[0]]
        res = 1
        while right < len(s):
            while s[right] in substr:
                substr.pop(0)
                left += 1
            substr.append(s[right])
            res = max(res, len(substr))
            right += 1
        return res
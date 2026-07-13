class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        length = 0
        unique = set()
        left, right = 0, 0

        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            length = max(length, len(unique))
            right += 1

        return length
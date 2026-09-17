class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        length = 0
        left = 0
        right = 0

        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            length = max(length, len(unique))
            right += 1
        
        return length
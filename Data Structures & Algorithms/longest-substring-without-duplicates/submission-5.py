class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        unique = set()
        length = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                length = max(length, len(unique))
            else:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1
                unique.add(s[right])
            right += 1
        
        return length
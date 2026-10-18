class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        left, right = 0, 0
        length = 0
        sub = set()

        while right < len(s):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            length = max(length, len(sub))
            right += 1

        return length
            
            

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        pattern = "[a-zA-Z0-9]"
        while left < right:
            while left < right and not re.search(pattern, s[left]):
                left += 1
            while left < right and not re.search(pattern, s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
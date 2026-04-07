class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while not self.isAlphanumeric(s[left]) and left < right:
                left += 1
            while not self.isAlphanumeric(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isAlphanumeric(self, c: str) -> bool:
        cOrd = ord(c)
        return 48 <= cOrd <= 57 or 65 <= cOrd <= 90 or 97 <= cOrd <= 122

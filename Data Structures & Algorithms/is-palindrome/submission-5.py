class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not self.isAlphaNumeric(s[left]) and left < right:
                left += 1
            while not self.isAlphaNumeric(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isAlphaNumeric(self, c: str) -> bool:
        return re.search("[A-Za-z0-9]", c)
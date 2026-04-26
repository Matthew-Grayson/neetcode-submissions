class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
        "]": "[",
        "}": "{",
        ")": "("
        }

        for c in s:
            if c not in key:
                stack.append(c)
            elif stack and stack[-1] == key[c]:
                stack.pop()
            else:
                return False

        return not stack
        

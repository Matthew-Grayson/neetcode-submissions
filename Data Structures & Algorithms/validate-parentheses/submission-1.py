class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            "]":"[",
            "}":"{",
            ")":"("
            }
        stack = []
        for c in s:
            if c in key:
                if not stack or key[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
            
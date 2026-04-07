class Solution:
    def isValid(self, s: str) -> bool:
        # if left brace, append to stack
        # if right brace check for match at top of stack
        # return True if all right braces have a matching left brace and stack is empty
        key = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []

        for c in s:
            if c not in key:
                stack.append(c)
            else:
                if not stack or key[c] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack
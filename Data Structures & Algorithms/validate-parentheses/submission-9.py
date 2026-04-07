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
            elif stack:
                if key[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through string
        # if left brace append to stack
        # if right brace check top of stack for matching left brace and pop it
        # return true if iteration completes and stack is empty
        key = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c not in key:
                stack.append(c)
            elif not stack or stack[-1] != key[c]:
                return False
            else:
                stack.pop()

        return not stack


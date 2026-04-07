class Solution:
    def isValid(self, s: str) -> bool:
        bracketKey = {
            "]": "[",
            "}": "{",
            ")": "("  
        }
        stack = []
        for x in s:
            if x not in bracketKey:
                stack.append(x)
            else:
                if not stack or stack[-1] != bracketKey[x]:
                    return False
                stack.pop()
        return not stack
            
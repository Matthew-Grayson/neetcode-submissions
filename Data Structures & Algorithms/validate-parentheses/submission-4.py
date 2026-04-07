class Solution:
    def isValid(self, s: str) -> bool:
        bracketDict = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []
        for c in s:
            if c not in bracketDict:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracketDict[c]:
                    return False
                stack.pop()
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        bracketCompliments = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c not in bracketCompliments:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracketCompliments[c]:
                    return False
                stack.pop()
        return not stack
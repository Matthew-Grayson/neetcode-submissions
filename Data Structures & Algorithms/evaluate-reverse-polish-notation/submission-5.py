class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(a / b)
        }
        stack = []
        res = int(tokens[0])

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                res = operations[token](op1, op2)
                stack.append(res)
                
        return res

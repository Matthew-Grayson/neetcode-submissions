class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(a / b)
        }
        stack = []
        res = int(tokens[0])

        for token in tokens:
            if token in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                res = operators[token](op2, op1)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return res
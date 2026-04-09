class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", "-", "/", "*"}

        for token in tokens:
            if token in symbols:
                if token == "+":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 + op1
                    stack.append(result)
                elif token == "-":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 - op1
                    stack.append(result)
                elif token == "*":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = op2 * op1
                    stack.append(result)
                elif token == "/":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    result = int(op2 / op1)
                    stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()

        
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            match token:

                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    result = a + b
                    stack.append(result)

                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    result = a - b
                    stack.append(result)

                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    result = a * b
                    stack.append(result)

                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    result = int(a / b)
                    stack.append(result)

                case _:
                    stack.append(int(token))

        return stack[0]
        
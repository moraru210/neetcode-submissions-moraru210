class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                sec = stack.pop()
                fir = stack.pop()
                res = fir + sec
                stack.append(res)
            elif token == "-":
                sec = stack.pop()
                fir = stack.pop()
                res = fir - sec
                stack.append(res)
            elif token == "*":
                sec = stack.pop()
                fir = stack.pop()
                res = fir * sec
                stack.append(res)
            elif token == "/":
                sec = stack.pop()
                fir = stack.pop()
                res = int(fir / sec)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]
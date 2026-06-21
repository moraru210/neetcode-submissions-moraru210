class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                f, s = stack[-1], stack[-2]
                new = f + s
                stack.append(new)
            elif op == "C":
                stack.pop()
            elif op == "D":
                f = stack[-1]
                new = f * 2
                stack.append(new)
            else:
                stack.append(int(op))

        return sum(stack)

        
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if stack and op == "C":
                stack.pop()
            elif stack and op == "D":
                stack.append(2*int(stack[-1]))
            elif stack and op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(op))
        return sum(stack)


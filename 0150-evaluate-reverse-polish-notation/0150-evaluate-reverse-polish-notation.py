class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == "+":
                stack.append(stack.pop() + stack.pop())
            elif op == "*":
                stack.append(stack.pop() * stack.pop())
            elif op == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif op == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(op))
        return stack[0]
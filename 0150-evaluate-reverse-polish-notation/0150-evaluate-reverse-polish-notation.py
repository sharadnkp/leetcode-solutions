class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['*', "/", "-","+"]:
                stack.append(i)
            else:
                y = stack.pop()
                x = stack.pop()
                if i == "*":
                    stack.append(int(x)*int(y))
                elif i == "/":
                    stack.append(int(int(x)/int(y)))
                elif i == "+":
                    stack.append(int(x)+int(y))
                else:
                    stack.append(int(x)-int(y))
        return int(stack[-1])
class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)

            elif ch == ')':
                start = stack.pop()
                s[start+1:i] = s[start+1:i][::-1]
            

        s = [ch for ch in s if ch not in "()"]

        return "".join(s)
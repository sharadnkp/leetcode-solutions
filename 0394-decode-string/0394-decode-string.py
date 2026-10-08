class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        curr = ""
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                num_stack.append(num)
                str_stack.append(curr)

                num = 0
                curr = ""

            elif ch == "]":
                repeat = num_stack.pop()
                prev = str_stack.pop()

                curr = prev + curr * repeat

            else:
                curr += ch

        return curr
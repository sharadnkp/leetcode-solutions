class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        answer = []
        for ch in s:
            if not stack or ch != stack[-1][0]:
                stack.append([ch,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        for ch,count in stack:
            while count != 0:
                answer.append(ch)
                count -= 1
        return ''.join(answer)
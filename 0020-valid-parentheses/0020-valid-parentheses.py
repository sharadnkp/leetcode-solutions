class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(store[ch])
            else:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
        return not stack
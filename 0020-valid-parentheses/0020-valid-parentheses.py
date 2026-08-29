class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')',
                   '[':']',
                   '{':'}'}
        stack = []
        for ch in s:
            if ch not in "{[(":
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
            else:
                stack.append(mapping[ch])
        return not stack
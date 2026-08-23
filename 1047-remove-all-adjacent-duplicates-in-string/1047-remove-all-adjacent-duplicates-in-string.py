class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for ch in s:
            if len(result) == 0:
                result.append(ch)
            elif result[-1] != ch:
                result.append(ch)
            else:
                result.pop()
        return ''.join(result)
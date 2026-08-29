class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for ch in s:
            if not result:
                result.append(ch)
                continue
            if ch == result[-1]:
                result.pop()
                continue
            result.append(ch)
        return ''.join(result)
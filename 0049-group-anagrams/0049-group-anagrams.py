class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            c = tuple(sorted(word))
            if c not in d:
                d[c] = []
            d[c].append(word)
        return list(d.values())
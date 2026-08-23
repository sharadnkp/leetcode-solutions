class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for ch in t:
            freq[ch] = freq.get(ch,0)-1
        return all(value == 0 for value in freq.values())
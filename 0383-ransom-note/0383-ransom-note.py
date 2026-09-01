class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        for ch in ransomNote:
            dict1[ch] = dict1.get(ch,0)+1
        for ch in magazine:
            dict1[ch] = dict1.get(ch,0)-1
        for i in dict1.values():
            if i > 0:
                return False
        return True
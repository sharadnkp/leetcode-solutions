class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0)+1
        
        used = False
        result = 0

        for i in set(s):
            if count[i]%2 == 0:
                result += count[i]
            elif count[i]%2 == 1 and count[i]>2 and not used:
                result += count[i]
                used = True
            elif not used and count[i]<2:
                result += count[i]
                used = True
            else:
                result += count[i]-1
        
        return result
            

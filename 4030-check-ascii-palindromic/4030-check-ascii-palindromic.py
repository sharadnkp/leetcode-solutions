class Solution:
    def isPalindromic(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            a = ord(s[left])
            b = ord(s[right])

            for bit in range(8):
                left_bit = (a >> bit) & 1
                right_bit = (b >> (7 - bit)) & 1

                if left_bit != right_bit:
                    return False

            left += 1
            right -= 1

        return True
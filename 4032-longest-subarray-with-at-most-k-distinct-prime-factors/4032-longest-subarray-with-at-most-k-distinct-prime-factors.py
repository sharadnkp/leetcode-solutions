class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        spf = list(range(100001))
        for i in range(2, int(100000 ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, 100001, i):
                    if spf[j] == j:
                        spf[j] = i
        factors = []
        for num in nums:
            curr = []
            while num > 1:
                p = spf[num]
                curr.append(p)
                while num % p == 0:
                    num //= p
            factors.append(curr)
        count = {}
        distinct = 0
        left = 0
        ans = 0
        for right in range(n):
            for p in factors[right]:
                if p not in count or count[p] == 0:
                    distinct += 1
                count[p] = count.get(p, 0) + 1
            while distinct > k:
                for p in factors[left]:
                    count[p] -= 1
                    if count[p] == 0:
                        distinct -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        freq = {}
        for i in nums1:
            freq[i] = freq.get(i,0)+1
        for i in nums2:
            if freq.get(i,0)>0:
                result.append(i)
                freq[i] = 0
        return result
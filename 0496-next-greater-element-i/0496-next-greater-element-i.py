class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                resolved = stack.pop()
                next_greater[resolved] = i
            stack.append(i)

        for num in stack:
            next_greater[num] = -1
            
        return [next_greater[i] for i in nums1]
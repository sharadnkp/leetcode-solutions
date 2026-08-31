class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top_i = stack.pop()
                height = heights[top_i]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)

        n = len(heights)
        while stack:
            top_i = stack.pop()
            height = heights[top_i]
            width = n - stack[-1] - 1 if stack else n
            max_area = max(max_area, height * width)

        return max_area
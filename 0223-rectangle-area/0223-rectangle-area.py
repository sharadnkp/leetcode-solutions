class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left=max(ax1,bx1)
        right=min(ax2,bx2)
        bottom=max(ay1,by1)
        top=min(ay2,by2)
        overlap_length=right - left
        overlap_width=top - bottom
        overlap = 0
        if overlap_length>0 and overlap_width>0:
            overlap=overlap_length*overlap_width
        a=(ax2-ax1)*(ay2-ay1)
        b=(bx2-bx1)*(by2-by1)
        area=a+b-overlap
        return area
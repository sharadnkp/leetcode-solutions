class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left=max(ax1,bx1)
        right=min(ax2,bx2)
        bottom=max(ay1,by1)
        top=min(ay2,by2)
        dx=right - left
        dy=top - bottom
        overlap = 0
        if dx>0 and dy>0:
            overlap=dx*dy
        a=abs(ax2-ax1)*abs(ay2-ay1)
        b=abs(bx2-bx1)*abs(by2-by1)
        area=a+b-overlap
        return area
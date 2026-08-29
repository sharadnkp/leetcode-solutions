class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while alive and i<0 and stack and stack[-1]>0:
                if abs(i)>stack[-1]:
                    stack.pop()
                elif abs(i) == stack[-1]:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(i)
        return stack
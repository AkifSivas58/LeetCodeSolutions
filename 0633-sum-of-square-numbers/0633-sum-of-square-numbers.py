class Solution(object):
    def judgeSquareSum(self, c):
        for a in range(int(c ** 0.5) + 1):
            b = (c-a**2) ** 0.5
            if b % 1 == 0:
                return True
        return False
        
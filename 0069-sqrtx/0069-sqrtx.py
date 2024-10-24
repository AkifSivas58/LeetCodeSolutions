class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        m = 0
        while l <= r:
            m = (l+r)//2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1 
            else:
                r = m - 1
        
        return r
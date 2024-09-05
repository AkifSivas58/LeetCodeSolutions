class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        summ = mean * (n+m) - sum(rolls)
        if summ > n * 6 or summ < n:
            return []
        
        res = [summ // n] * n
        remainder = summ % n

        for i in range(remainder):
            res[i] += 1
        
        return res

        
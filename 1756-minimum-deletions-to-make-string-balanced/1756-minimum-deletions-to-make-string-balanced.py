class Solution(object):
    def minimumDeletions(self, s):
        n = len(s)
        b_before = [0] * (n + 1)
        a_after = [0] * (n + 1)
        
        for i in range(1, n + 1):
            b_before[i] = b_before[i - 1]
            if s[i - 1] == 'b':
                b_before[i] += 1
                
        for i in range(n - 1, -1, -1):
            a_after[i] = a_after[i + 1]
            if s[i] == 'a':
                a_after[i] += 1

        sol = float('inf')
        for i in range(n + 1):
            sol = min(sol, b_before[i] + a_after[i])
        
        return sol

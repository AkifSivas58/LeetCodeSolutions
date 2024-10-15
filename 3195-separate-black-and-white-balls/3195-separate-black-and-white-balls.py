class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        res = 0
        curr = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                curr += 1
            else:
                res += curr
        
        return res

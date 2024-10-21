class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sett = set()
        n = len(s)
        maxi = 0

        def backtrack(ind):
            nonlocal maxi
            if ind == n:
                maxi = max(maxi, len(sett))
                return
            
            curr = ""
            for i in range(ind, n):
                curr += s[i]
                if curr not in sett:
                    sett.add(curr)
                    backtrack(i + 1)
                    sett.remove(curr)
            

        backtrack(0)
        return maxi

        
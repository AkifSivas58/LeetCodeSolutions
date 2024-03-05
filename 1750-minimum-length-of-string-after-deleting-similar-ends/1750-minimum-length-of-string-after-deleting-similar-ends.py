class Solution(object):
    def minimumLength(self, s):
        l = 0
        r = len(s) - 1

        while s[l] == s[r] and l < r:

            currentl = s[l]
            while l < r and s[l] == currentl:
                l += 1
                if r-l == 1 and s[l] == s[r]:
                    return 0

            currentr = s[r]
            while l < r and s[r] == currentr:
                r -= 1
                if r-l == 1 and s[l] == s[r]:
                    return 0
        
        return len(s[l:r+1])

            
        
class Solution(object):
    def countGoodSubstrings(self, s):
        res = 0

        if len(s) < 2:
            return 0

        if len(s) == 3:
            chars = set()
            for char in s:
                if char in chars:
                    return 0
                chars.add(char)
                
            return 1

        for i in range(len(s)-2):
            chars = set()
            for char in s[i:i+3]:
                chars.add(char)
            if len(chars) == 3:
                res += 1

        return res
                
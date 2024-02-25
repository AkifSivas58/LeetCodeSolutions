class Solution(object):
    def printVertically(self, s):
        words = s.split()
        max_length = max(len(word) for word in words)
        
        res = [""] * max_length
        for word in words:
            for i in range(len(word)):
                res[i] += word[i]
            if len(word) < max_length:
                for j in range(len(word), max_length):
                    res[j] += " "

        res = [word.rstrip() for word in res]
        return res
                
                     
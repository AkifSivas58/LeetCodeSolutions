class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        res = []
        for word in words:
            curr = word.split(separator)
            for c in curr:
                if c != "":
                    res.append(c)
            
        
        return res
        
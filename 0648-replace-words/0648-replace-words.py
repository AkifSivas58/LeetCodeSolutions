class Solution(object):
    def replaceWords(self, dictionary, sentence):
        dicts = set(dictionary)
        words = sentence.split()
        res = ""
        for word in words:
            current = ""
            for ch in word:
                current = current + ch
                if current in dicts:
                    res = res + current + " "
                    break
            
            if current in dicts:
                continue
            res = res + current + " "
        
        return res.rstrip()
                
        
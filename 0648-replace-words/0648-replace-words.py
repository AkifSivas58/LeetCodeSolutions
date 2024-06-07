class Solution(object):
    def replaceWords(self, dictionary, sentence):
        dicts = set(dictionary)
        words = sentence.split()
        res = []
        
        for word in words:
            current = ""
            found = False
            for ch in word:
                current += ch
                if current in dicts:
                    res.append(current)
                    found = True
                    break
            
            if not found:
                res.append(word)
        
        return " ".join(res)
                
        
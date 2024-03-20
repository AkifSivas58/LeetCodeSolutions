class Solution(object):
    def checkIfPangram(self, sentence):
        found = set()

        for char in sentence:
            found.add(char)
        
        if len(found) == 26:
            return True
        
        return False
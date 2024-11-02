class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if words[0][0] != words[len(words) - 1][-1]:
            return False
            
        for i in range(1, len(words)):
            if words[i-1][-1] != words[i][0]:
                return False
        
        return True
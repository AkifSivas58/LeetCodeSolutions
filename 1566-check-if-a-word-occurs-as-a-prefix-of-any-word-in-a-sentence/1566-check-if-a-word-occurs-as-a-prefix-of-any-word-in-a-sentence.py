class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for i in range(len(words)):
            if len(words[i]) >= len(searchWord):
                found = True
                for j in range(len(searchWord)):
                    if words[i][j] != searchWord[j]:
                        found = False
                        break
                
                if found:
                    return i + 1
        
        return -1


                    
                    

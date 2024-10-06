class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        l, r = 0, 0
        while l < len(s1) and r < len(s2):
            if s1[l] != s2[r]:
                break
            
            s1.pop(l)
            s2.pop(r)
            

        l, r = len(s1)-1, len(s2) - 1
        while l > -1 and r > -1:
            if s1[l] != s2[r]:
                break

            s1.pop(l)
            s2.pop(r)
            l -= 1
            r -= 1
            
        
        if not s1 or not s2:
            return True
        
        return False
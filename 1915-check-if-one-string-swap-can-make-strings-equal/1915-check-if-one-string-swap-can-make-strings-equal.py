from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        summ = 0
        ind1 = 0
        ind2 = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if summ == 0:
                    ind1 = i
                elif summ == 1:
                    ind2 = i

                summ += 1
        
        if (summ == 2 and (s1[ind1] == s2[ind2] and s1[ind2] == s2[ind1])) or summ == 0:
            return True
        
        return False

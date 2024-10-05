class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counts_1 = dict()
        for c in s1:
            if c in counts_1:
                counts_1[c] += 1
            else:
                counts_1[c] = 1
        
        counts_2 = dict()
        for c in s2[:n]:
            if c in counts_2:
                counts_2[c] += 1
            else:
                counts_2[c] = 1

        for i in range(len(s2)-n):
            if counts_1 == counts_2: 
                return True

            if counts_2[s2[i]] == 1:
                del counts_2[s2[i]]
            else:
                counts_2[s2[i]] -= 1

            if s2[n+i] in counts_2:
                counts_2[s2[n+i]] += 1
            else:
                counts_2[s2[n+i]] = 1
        
        if counts_1 == counts_2: 
            return True
        
        return False
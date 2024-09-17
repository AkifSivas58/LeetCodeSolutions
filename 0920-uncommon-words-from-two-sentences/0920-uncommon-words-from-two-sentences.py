from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = defaultdict(int)
        for word in s1.split(" "):
            counts[word] += 1
        
        for word in s2.split(" "):
            counts[word] += 1

        res = []
        for word in counts.keys():
            if counts[word] == 1:
                res.append(word)
        
        return res
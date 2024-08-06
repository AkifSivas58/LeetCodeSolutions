from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        freq = Counter(word)

        sorted_freq = sorted(freq.values(), reverse=True)
        
        min_presses = 0
        for i in range(len(sorted_freq)):
            keypresses = (i // 8) + 1  
            min_presses += keypresses * sorted_freq[i]
        
        return min_presses
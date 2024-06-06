from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        occurences = Counter(hand)

        sorted_keys = sorted(occurences.keys())
        for key in sorted_keys:
            while occurences[key] > 0:
                for i in range(groupSize):
                    if occurences[key + i] > 0:
                        occurences[key + i] -= 1
                    else:
                        return False

        return True
        
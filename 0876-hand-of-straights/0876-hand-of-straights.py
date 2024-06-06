class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        occurences = {}
        for num in hand:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1

        hand.sort()
        while len(hand) != 0:
            num = hand.pop(0)
            occurences[num] -= 1

            for i in range(1, groupSize):
                if num+i in occurences and occurences[num+i] != 0:
                    occurences[num+i] -= 1
                    hand.remove(num+i)
                else:
                    return False

        return True


        